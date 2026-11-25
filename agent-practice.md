# How the team works with skills and checks the agent

**Task for the first working session.** A customer ordered 10 units; the warehouse shipped 6. Sales ask for a new status. Can we already promise the customer that they will see the remainder for every line? The business analyst answers first, then gives the same analysis to an agent. We compare the grounds of the two answers and the question each would take to the product owner.

## What the agent receives at each moment

The [OKF catalogue](okf/index.md) holds the training materials in the order they appeared. The input for the 6 October exercise is only the [source records](okf/intake.md). At the next step the results of the [architecture check](okf/prototype.md) appear. Later the team issues the [decision](okf/decision.md), the [new requirement version](okf/requirement.md), the [observations on the build](okf/observations.md) and the [acceptance record](okf/acceptance.md). For the pre-acceptance exercise, give the agent the requirement and the observations on build b17. Open record A-01 after it answers. When reviewing a past project, give the agent only the materials available **at the moment of the decision**. Otherwise it is easy to guess, from the finished record, the answer to a question that was still open on that day.

| When and who delegates the work | What the skill does | What the person checks and decides |
|---|---|---|
| 6 October. The business analyst prepares a meeting with the product owner | [Clarify requirement](.agents/skills/clarify-requirement/SKILL.md) compares the original commitment with the sales request. It proposes a distinguishing example for the “first shipment” and “remainder per line” options. | The analyst checks the statements against the sources. The product owner chooses the behaviour. The architect checks where the data will come from. |
| 7 October. The project manager has the prototype result and the assignees' estimates | [Trace change impact](.agents/skills/trace-change-impact/SKILL.md) finds the affected WBS packages, compares two schedule branches and calculates the change in labour cost. | The assignees check the estimates. The project manager confirms the calculation. The sponsor accepts the budget and the date; the analyst links the new version to the decision record. |
| Before acceptance. The tester prepares the package for the product owner | [Prepare acceptance](.agents/skills/prepare-acceptance/SKILL.md) describes the expected states from the version in force and matches them with what was recorded on a specific build. | The tester reproduces the scenario and attaches the observations. The product owner accepts the delivery or returns it with comments. |

**The first prompt can be used verbatim.** “Use the `clarify-requirement` skill. You have records I-01 and I-02 as of the end of 6 October. Prepare a short card for the product owner. What has already been agreed, which options will the customer be able to tell apart in an order of 10 units after a first shipment of 6, and what still needs to be checked with the warehouse? Give the basis for every conclusion.” Pass the skill instructions and the two records in a separate session with a restricted set of materials.

A usable draft keeps the agreed rule on the accounting status, explains the limits of the existing exchange and leaves the choice of option to the owner. If the answer immediately promises a visible remainder of 4, send the analyst a specific question: “Which approved record and which data source does this promise rest on?” The number 4 is arithmetically correct, but by itself it says nothing about the team's commitment.

## How the evals work

An eval is a separate task with known inputs and predefined criteria for checking the answer. The set has six self-contained tasks on partial shipments. Their numbers and decisions change from task to task. They show whether the agent follows the materials it was given, even when the correct answer differs from the worked example.

| Task pair | The error we look for | Sign of a usable answer |
|---|---|---|
| REQ-1, REQ-2. Requirement decision | Treating a newer request as a scope change, or confusing data availability with approval of a feature | With no decision, the question stays with the owner. With a signed decision, the agent states the approved scope and keeps the late request as a proposal. |
| PLAN-1, PLAN-2. Re-planning | Adding all person-days to the duration, or naming an exact date when the duration of one branch is unknown | The agent builds the network and separates effort from calendar time. With an incomplete estimate it gives a lower bound on the date and the missing estimate, and keeps the current commitment in force. |
| ACC-1, ACC-2. Testing and acceptance | Adding the same shipment again, inventing the last observation or declaring the delivery accepted | The agent shows the quantity after each message, ties the actual result to the build and names the basis for the acceptance decision. |

**How to use the result.** The consultant and the team choose which error would break the hand-over of the result to the next participant. For example, publishing an unapproved commitment is critical even if all other fields are correct. The reviewer gives the agent the input and the skill, saves the answer, runs the field check and reads the explanation against the rubric. They record the skill version, the model, the date and the specific error. After a fix, they re-run both the problem task and the other five. When the model or the sources change, the procedure can be reproduced. [Run commands and review rules](evals/README.md)

**Where I come in.** In the first session I help the analyst frame the fork and, together with the architect and the project manager, trace the consequences of both options. Then I prepare tasks and criteria with the team on disputed decisions, run the review of discrepancies and hand the skills over to the staff. On the next change the analyst runs the procedure independently. At the closing meeting we check who found the error, how long proofreading took and what materials the person needed to decide.
