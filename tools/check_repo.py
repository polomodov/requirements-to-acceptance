"""Repository checks run in CI: relative links resolve, and the EN and RU eval sets match.

    python3 tools/check_repo.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_links():
    errors = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = (md.parent / target.split("#")[0]).resolve()
            if not path.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link {target}")
    return errors


def check_evals():
    errors = []
    load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))
    en_t, ru_t = load("evals/tasks.json"), load("ru/evals/tasks.json")
    en_c, ru_c = load("evals/criteria.json"), load("ru/evals/criteria.json")
    if en_t["cases"].keys() != ru_t["cases"].keys():
        errors.append("EN and RU task IDs differ")
    for case_id, case in en_t["cases"].items():
        other = ru_t["cases"].get(case_id, {})
        if case["skill"] != other.get("skill") or case["sources"].keys() != other.get("sources", {}).keys():
            errors.append(f"{case_id}: skill or source IDs differ between EN and RU")
    for skill, fields in en_t["formats"].items():
        if fields.keys() != ru_t["formats"].get(skill, {}).keys():
            errors.append(f"{skill}: answer fields differ between EN and RU")
    for case_id in en_c:
        if en_c[case_id]["expected"] != ru_c.get(case_id, {}).get("expected"):
            errors.append(f"{case_id}: expected values differ between EN and RU")
    for skill_dir in sorted((ROOT / ".agents/skills").iterdir()):
        if not (ROOT / "ru/.agents/skills" / skill_dir.name / "SKILL.md").exists():
            errors.append(f"skill {skill_dir.name} has no Russian version")
    return errors


def main():
    errors = check_links() + check_evals()
    for error in errors:
        print(error)
    print("OK" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
