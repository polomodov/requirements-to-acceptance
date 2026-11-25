"""Issue the eval tasks and grade the structured part of an answer file.

Выдача заданий и проверка структурированной части ответа.
"""

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA = {"en": ROOT / "evals", "ru": ROOT / "ru" / "evals"}

TEXT = {
    "en": {
        "description": "Issue the eval tasks and grade the structured part of an answer file.",
        "show": "Print one task or the whole set, without the key.",
        "grade": "Grade a JSON file with answers.",
        "case": "Task ID; can be repeated.",
        "lang": "Language of the task set: en (default) or ru.",
        "duplicate": "Duplicate JSON key: {}",
        "not_object": "The answer must be a JSON object keyed by task IDs.",
        "unexpected": "The answer contains tasks outside the selected set: ",
        "missing": "{} — missing",
        "mismatch": "{} — expected {}, got {}",
        "note": "note — an explanation for the reviewer is required",
        "no_answer": "answer object is missing",
        "failed": "{}  missing field or mismatch",
        "passed": "{}  fields match",
        "total": "Automated part: {}/{}. The reviewer grades the explanations.",
        "unknown": "Unknown IDs: ",
        "error": "Error: {}",
        "instruction": (
            "Apply the named skill to each task separately. Return one JSON object keyed by task ID. "
            "Each ID maps to an object with every field from answer_fields, including the note. "
            "Write numbers, arrays, booleans and null as JSON types. Each task uses only its own sources."
        ),
    },
    "ru": {
        "description": "Выдача заданий и проверка структурированной части ответа.",
        "show": "Напечатать задание или весь набор без ключа.",
        "grade": "Оценить JSON с ответами.",
        "case": "ID задания, можно повторить.",
        "lang": "Язык набора заданий: en (по умолчанию) или ru.",
        "duplicate": "Повторён ключ JSON: {}",
        "not_object": "Ответ должен быть объектом JSON с идентификаторами заданий.",
        "unexpected": "Ответ содержит задания вне выбранного набора: ",
        "missing": "{} — пропуск",
        "mismatch": "{} — ожидается {}, получено {}",
        "note": "note — нужно пояснение для рецензента",
        "no_answer": "отсутствует объект ответа",
        "failed": "{}  пропуск или расхождение",
        "passed": "{}  поля совпали",
        "total": "Автоматическая часть: {}/{}. Обоснования оценивает рецензент.",
        "unknown": "Неизвестные ID: ",
        "error": "Ошибка: {}",
        "instruction": (
            "Примените указанный скилл отдельно к каждому заданию. Верните один JSON-объект с ID заданий в ключах. "
            "Каждому ID соответствует объект со всеми полями answer_fields, включая пояснение note. "
            "Числа, массивы, логические значения и null пишите в типах JSON. В каждом задании используются только его источники."
        ),
    },
}


def read_json(path, t):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(t["duplicate"].format(key))
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


def grade(answers, selected, criteria, t):
    if not isinstance(answers, dict):
        raise ValueError(t["not_object"])
    unexpected = answers.keys() - set(selected)
    if unexpected:
        raise ValueError(t["unexpected"] + ", ".join(sorted(unexpected)))
    passed = 0
    for case_id in selected:
        answer = answers.get(case_id)
        errors = []
        if isinstance(answer, dict):
            for key, expected in criteria[case_id]["expected"].items():
                if key not in answer:
                    errors.append(t["missing"].format(key))
                elif not same_value(answer[key], expected):
                    errors.append(t["mismatch"].format(
                        key, json.dumps(expected, ensure_ascii=False), json.dumps(answer[key], ensure_ascii=False)))
            if not isinstance(answer.get("note"), str) or not answer["note"].strip():
                errors.append(t["note"])
        else:
            errors.append(t["no_answer"])
        if errors:
            print(t["failed"].format(case_id))
            for error in errors:
                print(f"  {error}")
        else:
            print(t["passed"].format(case_id))
            passed += 1
    print(t["total"].format(passed, len(selected)))
    return 0 if passed == len(selected) else 1


def main(argv=None):
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--lang", choices=sorted(DATA), default="en")
    lang = pre.parse_known_args(argv)[0].lang
    t = TEXT[lang]

    parser = argparse.ArgumentParser(description=t["description"], parents=[pre])
    commands = parser.add_subparsers(dest="command", required=True)
    show = commands.add_parser("show", help=t["show"])
    score = commands.add_parser("grade", help=t["grade"])
    score.add_argument("answers", type=Path)
    for command in (show, score):
        command.add_argument("--case", action="append", dest="cases", help=t["case"])
    args = parser.parse_args(argv)

    try:
        tasks = read_json(DATA[lang] / "tasks.json", t)
        selected = list(dict.fromkeys(args.cases or tasks["cases"]))
        unknown = set(selected) - tasks["cases"].keys()
        if unknown:
            parser.error(t["unknown"] + ", ".join(sorted(unknown)))
        if args.command == "grade":
            return grade(read_json(args.answers, t), selected, read_json(DATA[lang] / "criteria.json", t), t)

        packet = {}
        for case_id in selected:
            case = tasks["cases"][case_id]
            packet[case_id] = {**case, "answer_fields": tasks["formats"][case["skill"]]}
        print(json.dumps({"instruction": t["instruction"], "tasks": packet}, indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError) as error:
        print(t["error"].format(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
