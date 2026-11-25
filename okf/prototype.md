---
type: Experiment
title: E-01. Test-bench experiment and work estimates
status: stable
sources:
  - resource: intake.md
---

# E-01. Experiment log, 7 October 2026

**The architect's question.** Can the warehouse log distinguish two shipments from two deliveries of the same document? The reason for the check is the warehouse representative's remark. [I-02](intake.md)

**Conditions.** The architect and the warehouse representative opened the log of posted, immutable records for one warehouse. Order Z-70 has one line, L1, for 10 pumps. Below are three deliveries for the same order. The shipment document number and the order line are payload fields; the delivery number is the record ID in the exchange log.

| Delivery | Shipment document | Order line | Quantity | Posted |
|---|---|---|---:|---|
| E-101 | S-81 | L1 | 6 | Yes |
| E-102 | S-81 | L1 | 6 | Yes |
| E-103 | S-83 | L1 | 4 | Yes |

**Observation.** The sum of the three messages is 16. Counting each “shipment document + order line” pair once, the prototype produced 6, 6, 10 in turn. The boundary of this key in the experiment is one warehouse and one order. The architect confirmed the required fields exist on the test bench. Reversals, corrections and the exchange inside the delivered build were not part of this experiment.

## Estimate sheet for the 7 October meeting

The project manager collected the assignees' estimates for option B: load quantities and show the remainder for each line. Option A only adds a marker for the first posted document. Both options require a connection to the log. The figures below cover the original plan and option B.

| Package and activity | Assignee | After | Full duration in baseline, working days | Full duration with option B, working days |
|---|---|---|---:|---:|
| 1.1 / A. Agree the scenario | Business analyst | — | 1 | 1 |
| 1.1 / B. Check the data on the test bench | Architect | A | 2 | 2 |
| 1.2 / C. Build the screen | Portal developer | A | 3 | 6 |
| 1.3 / D. Load data and calculate the state | Integration developer | B | 4 | 6 |
| 1.4 / E. Build the release and test the scenarios | Tester | C, D | 2 | 3 |
| 1.4 / F. Present the release | Project manager | E | 1 | 1 |

Counting from 5 October 2026, working days Monday to Friday. Each activity takes one assignee full time. C and D are done by different people. The next activity starts on the first working day after all its predecessors finish. The estimates include work already done by the date of the meeting. The rate for labour cost is 500 euros per person-day. When the sheet was prepared, the choice of option and the change to the baseline were still open.
