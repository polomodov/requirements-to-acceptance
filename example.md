# Partial shipments in a B2B ordering portal

A customer ordered 10 pumps. The warehouse shipped 6; the other 4 will go on another truck. The next morning the customer's account still shows “Open”. The customer calls the account manager with two different questions. Has anything shipped at all? How many pumps have not shipped yet?

This is a fictional delivery of a portal for wholesale customers. All documents, observations, dates and estimates were created for the walkthrough. The product owner's goal is to reduce the number of enquiries about remaining quantities. They will be able to check the effect after launch by comparing the number of such enquiries per 100 partially shipped orders before and after the change.

## 1. Reconstruct the original commitment

On 5 October 2026 the product owner approved **R-01, version 1**. On the order card the customer sees the accounting status “Open” or “Closed”. The source is the closed flag in the accounting system. The project manager fixed a baseline with acceptance on 16 October. The next day sales asked for a “Partially shipped” status. The warehouse representative pointed out that a shipment document can arrive twice, and that an order is sometimes closed in accounting later than the physical shipment.

The business analyst kept the request and the comment next to the approved version. For the product owner, the analyst framed the choice: is it enough to say that shipping has started, or should the customer see the shipped quantity and the remainder for every line? Neither value can be reliably derived from the existing field. [Source records I-01 and I-02](okf/intake.md)

## 2. Test the architectural risk

During the RUP elaboration phase, the architect and a warehouse specialist reproduced the exchange on the test bench. The log of posted shipments contains the order, the order line, the shipment number and the quantity. A repeated message keeps the shipment number and the line. In the test order, a record for 6 units arrived first, then the same record again, then a new record for 4. A simple sum gave 16. The prototype counted each “shipment number + order line” pair once and got 10. These rules hold for posted immutable records within one warehouse and order. Reversals and corrections need a separate rule.

The architect presented two options. **A. First-shipment fact.** Show a marker on the order after the first posted document. The customer learns that shipping has started but has to ask the account manager for the exact remainder. **B. Quantities per line.** Store unique shipment lines, match them to order lines and show the shipped quantity and the remainder. Both options need access to the log. The prototype confirmed the data structure on the test bench. Bringing the exchange into the build and the end-to-end test remained in the plan. [Observations E-01](okf/prototype.md)

## 3. Decide on scope and commitments

On 7 October the product owner chose **B**. After a posted shipment on a line of 10 units, the portal must show “Shipped 6, remaining 4”. The state of the whole order is “Partially shipped”. After all lines have shipped in full, “Shipped”. Before the first shipment, “Awaiting shipment”. The accounting status remains a separate field. The date of the next truck, returns, reversals and cancellations were left out of this delivery. The analyst kept the separate sales request to promise the next shipment date as an open item.

The project manager presented the calculation below. The sponsor, who is responsible for budget and date, approved an extra 3,000 euros in the labour budget and acceptance on 21 October. After both approvals the analyst issued **R-01, version 2**, referencing **D-01**. The architect linked the de-duplication rule to this version. The work packages and tests got the same basis. [Decision D-01](okf/decision.md) · [Requirement R-01 in force](okf/requirement.md)

## 4. Recalculate work, schedule and cost

The top-level WBS deliverable is an accepted order card. The project manager and the assignees identified four packages. **1.1** delivers an agreed scenario and a verified exchange model (A, B). **1.2**, the customer screen (C). **1.3**, the data and the state calculation for that screen (D). **1.4**, a tested build and the acceptance record (E, F). For option B, 1.2 gained per-line quantities, 1.3 gained reading shipment lines and protection against double counting, and 1.4 gained additional tests. The owner of each package confirmed the remaining estimate.

Working days are Monday to Friday. Each activity takes one assignee full time. The screen and the exchange are built by different people. The next activity starts on the working day after all predecessors finish. The table shows the full duration of activities, including work done by 7 October. All dates are in October 2026.

| Activity | After | Duration before → after, working days | Original plan | Per D-01 |
|---|---|---:|---|---|
| A. Agree the original scenario | — | 1 → 1 | 5 | 5 |
| B. Check the available data on the test bench | A | 2 → 2 | 6–7 | 6–7 |
| C. Build the customer screen | A | 3 → 6 | 6–8 | 6–13 |
| D. Implement data loading and calculation | B | 4 → 6 | 8–13 | 8–15 |
| E. Build the release and test the scenarios | C, D | 2 → 3 | 14–15 | 16–20 |
| F. Present the release to the product owner | E | 1 → 1 | 16 | 21 |

**Summary for the sponsor.** Effort grew from 13 to 19 person-days. At an internal rate of 500 euros per person-day, labour cost grew from 6,500 to 9,500 euros. The critical path A–B–D–E–F grew from 10 to 13 working days. The screen is ready on 13 October and has two working days of float before D finishes. That is why six extra person-days move acceptance by three working days. Until D-01 was approved, “21 October” was a forecast. With the sponsor's decision of 7 October it entered the updated baseline.

## 5. Present the result and trace back its basis

The tester checked build **b17** on the integration test bench. In each scenario the tester waited for the input documents to be processed, refreshed the customer's card and recorded the values shown. T-01 to T-03 use an order with one line for 10 units. T-04 starts with a separate order. All observations below are part of the training example.

| Check | Expected per R-01, v. 2 | What the tester saw |
|---|---|---|
| T-01. Before shipment, then a document for 6 | First 0/10 and “Awaiting shipment”, then 6/4 and “Partially shipped”. The first number is shipped, the second is remaining | After refreshing the card, both pairs of numbers and both states matched the expectation |
| T-02. Repeat of the same document for 6 | The line still shows 6/4; the order state does not change | The log recorded the repeated delivery. The screen still showed 6/4 and “Partially shipped” |
| T-03. New document for the remaining 4 | The line shows 10/0, “Shipped”. If the accounting closure has not arrived yet, the accounting status stays “Open” | Both states are visible at once; the order line shows 10/0 |
| T-04. One document has lines for two order lines; ordered 2 and 3, shipped 2 and 1 | Lines show 2/0 and 1/2. The whole order is “Partially shipped” | Both lines of the one document were counted; the order state matched the expectation |

On 21 October the product owner checked the results against version 2 and accepted the delivery in **A-01**. From T-02 you can go back from the observation “6/4 after the repeat” to the criterion in R-01, the de-duplication in package 1.3 and the test-bench observation E-01. D-01 shows who put this work into the delivery and accepted the consequences for budget and date. [Observations T-01–T-04](okf/observations.md) · [Record A-01](okf/acceptance.md)
