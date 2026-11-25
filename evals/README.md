# How to test the three skills on partial shipments

The six tasks reproduce decisions made by the analyst, the project manager and the product owner. Within each pair a material condition changes. The point of the check is to see whether the agent changes its conclusion when the sources change. All inputs are fictional. Each task uses its own source data and versions.

| Skill | Tasks | What changes |
|---|---|---|
| [Clarify requirement](../.agents/skills/clarify-requirement/SKILL.md) | REQ-1, REQ-2 | Which data is transmitted, and whether there is a decision on the first release |
| [Trace change impact](../.agents/skills/trace-change-impact/SKILL.md) | PLAN-1, PLAN-2 | Whether the estimate of one of two parallel activities is known or still being clarified |
| [Prepare acceptance](../.agents/skills/prepare-acceptance/SKILL.md) | ACC-1, ACC-2 | Where the repeated event falls in the history, how complete the observations are, and whether there is an acceptance record |

## Run

Run the commands from the repository root. Python 3.7+ with the standard library is enough.

```sh
python3 evals/run.py show > /tmp/shipment-tasks.json
```

In a new session, give the agent the export and the three skill files. Keep the key and the walkthrough materials with the reviewer. Ask for one JSON in the format from the export. Save it as `/tmp/shipment-answers.json` and grade it.

```sh
python3 evals/run.py grade /tmp/shipment-answers.json
```

For a single task, add the same option to **both** commands, for example `--case PLAN-2`. A missing task or required field fails the automated part. Exit code 0 means the answers match on the checked fields, 1 means discrepancies, 2 means an input or command error. Issuing tasks reads only the [source data](tasks.json). Grading uses the [key and reviewer notes](criteria.json).

The same tasks in Russian live in [`ru/evals/`](../ru/evals/README.md). Add `--lang ru` before the command (`python3 evals/run.py --lang ru show`) and give the agent the Russian skills from `ru/.agents/skills/`. The expected values are identical in both languages, so results are comparable.

## Reviewing an answer

Each task has two results. The script checks types, values, the order of events and the presence of an explanation. The reviewer reads the `note` field using the `review` criterion from the key. To pass, the explanation must meet three checks.

1. **Sources.** Material claims rest on specific records from the task. The author distinguishes a participant's words, an approved decision and a system observation.
2. **Reasoning.** A colleague can follow the choice of option, the calculation or the test from the answer. The claims agree with the structured fields. The assumptions the result depends on are stated.
3. **Action.** The recipient understands what they can do based on the answer. If a decision, an estimate or an observation is missing, the specific gap and how to close it are named.

If any check fails, mark it and keep the phrase that led to the verdict. For example, the number of shipped units may be calculated correctly, but the phrase “the last event was processed successfully” with no observation behind it fails the manual review. For a repeat run, record the date, the skill and task versions, the model or agent with its exact version, the answers received, and separately the script results and the reviewer's verdicts. The six tasks give a regression check for these situations. Transferring the method to another process needs examples from that process.

## Example result from 25 November 2026

In one separate session, a Codex agent received the six tasks **in Russian** and the texts of the three Russian skills, without the key and the worked case. The exact model version was not recorded for this run; future runs should record it. The automated check passed **6 of 6** answers. A second AI reviewer checked the source references, the reasoning and the next action. It passed all six explanations and flagged an ambiguous way of writing quantity and remainder with a slash. For a product owner, “shipped 10, remaining 0” is clearer. The saved answers keep the original wording. [Agent answers](../ru/evals/runs/2026-11-25-answers.json)

In PLAN-1 the agent saw that two extra days of adapter work fit into the float of the parallel branch. In ACC-1 it calculated the remainder after the last shipment and separately noted that there was no observation on the build under test. This is one run of a fixed set. There is no English-language run yet. The value of the skills for a particular team can only be judged on its own examples and against its usual way of working.

```sh
python3 evals/run.py --lang ru grade ru/evals/runs/2026-11-25-answers.json
```
