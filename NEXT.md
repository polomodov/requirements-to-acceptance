# Where to dig next

This repository shows the concept on one fictional delivery, three skills and six evals. It is a starting point, not a finished product. Below are the directions that look most promising, each with the question it should answer and a first step. Ideas, issues and pull requests are welcome.

## 1. Automate the review of explanations

**Question.** Can an LLM judge grade the `note` field against the rubric as reliably as a human reviewer?

**First step.** Collect 30–50 answers with human verdicts on the three rubric checks (sources, reasoning, action), then measure the judge's agreement with them. Keep the script check and the judge as separate results.

## 2. Grow the eval set and compare models

**Question.** Which errors do current models make most often, and do the skills actually reduce them?

**First step.** Add paired tasks for reversals, several warehouses, conflicting authorities and stale sources. Run each model with and without the skills, in English and in Russian, and record the model version, date and skill version for every run. The only saved run so far is one Russian-language run from 25 November 2026.

## 3. Move from a fictional case to a real process

**Question.** Does the method reduce rework on a real team?

**First step.** Pick one completed change and one upcoming change in a real project. Measure how often tasks go back for clarification after development starts and how long the analyst spends proofreading agent output. Compare against the team's usual way of working.

## 4. Tooling for an OKF dossier with a cut-off date

**Question.** How do you give an agent only the records that existed at the moment of a decision?

**First step.** A small tool that reads the OKF catalogue and builds a context packet “as of date X”, with a check that no later record leaks in. Today this is done by hand following the table in [okf/index.md](okf/index.md).

## 5. Automatic checking of trace links

**Question.** Can the links requirement → work package → test → acceptance record be checked automatically when a requirement version changes?

**First step.** Describe the links as structured fields in the OKF cards and write a check that lists dependent elements that have not been re-confirmed for the new version, in the spirit of the old Rational Rose and RequisitePro integration.

## 6. Make the case harder

**Question.** Where does the de-duplication key “shipment number + order line” stop working?

**First step.** Add reversals, corrections, several warehouses and partial cancellations as a second delivery with its own decision, plan and acceptance.

## 7. Connect to the tools teams already use

**Question.** What is the smallest integration with a tracker or requirements register that keeps the chain intact?

**First step.** Map the minimal record from [method.md](method.md) to fields in one popular issue tracker and try it on a pilot.

## Open questions

- Who owns a trace link when one architecture decision serves several requirements in different deliveries?
- How detailed should the record be for a small team, and what is the signal that it is time to add detail?
- How do you show an agent the authority matrix without letting it treat a confident message in chat as a decision?
- Which measure of the method's effect is cheap enough to collect on every change?
