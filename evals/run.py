"""Локальная выдача заданий и проверка структурированной части ответа."""

import argparse
import json
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent


def read_json(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Повторён ключ JSON: {key}")
            result[key] = value
        return result

    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def same_value(actual, expected):
    if isinstance(expected, list):
        return (isinstance(actual, list) and len(actual) == len(expected)
                and all(same_value(a, e) for a, e in zip(actual, expected)))
    if type(expected) in (int, float):
        return type(actual) in (int, float) and actual == expected
    return type(expected) is type(actual) and actual == expected


def grade(answers, selected, criteria):
    if not isinstance(answers, dict):
        raise ValueError("Ответ должен быть объектом JSON с идентификаторами заданий.")
    unexpected = answers.keys() - set(selected)
    if unexpected:
        raise ValueError("Ответ содержит задания вне выбранного набора: " + ", ".join(sorted(unexpected)))
    passed = 0
    for case_id in selected:
        answer = answers.get(case_id)
        errors = []
        if isinstance(answer, dict):
            for key, expected in criteria[case_id]["expected"].items():
                if key not in answer:
                    errors.append(f"{key} — пропуск")
                elif not same_value(answer[key], expected):
                    errors.append(f"{key} — ожидается {json.dumps(expected, ensure_ascii=False)}, "
                                  f"получено {json.dumps(answer[key], ensure_ascii=False)}")
            if not isinstance(answer.get("note"), str) or not answer["note"].strip():
                errors.append("note — нужно пояснение для рецензента")
        else:
            errors.append("отсутствует объект ответа")
        if errors:
            print(f"{case_id}  пропуск или расхождение")
            for error in errors:
                print(f"  {error}")
        else:
            print(f"{case_id}  поля совпали")
            passed += 1
    print(f"Автоматическая часть: {passed}/{len(selected)}. Обоснования оценивает рецензент.")
    return 0 if passed == len(selected) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    show = commands.add_parser("show", help="Напечатать задание или весь набор без ключа.")
    score = commands.add_parser("grade", help="Оценить JSON с ответами.")
    score.add_argument("answers", type=Path)
    for command in (show, score):
        command.add_argument("--case", action="append", dest="cases", help="ID задания, можно повторить.")
    args = parser.parse_args()

    tasks = read_json(BASE / "tasks.json")
    selected = list(dict.fromkeys(args.cases or tasks["cases"]))
    unknown = set(selected) - tasks["cases"].keys()
    if unknown:
        parser.error("Неизвестные ID: " + ", ".join(sorted(unknown)))
    if args.command == "grade":
        return grade(read_json(args.answers), selected, read_json(BASE / "criteria.json"))

    packet = {}
    for case_id in selected:
        case = tasks["cases"][case_id]
        packet[case_id] = {**case, "answer_fields": tasks["formats"][case["skill"]]}
    print(json.dumps({
        "instruction": "Примените указанный скилл отдельно к каждому заданию. Верните один JSON-объект с ID заданий в ключах. Каждому ID соответствует объект со всеми полями answer_fields, включая пояснение note. Числа, массивы, логические значения и null пишите в типах JSON. В каждом задании используются только его источники.",
        "tasks": packet,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(2)
