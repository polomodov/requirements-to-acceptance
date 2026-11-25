---
type: Test record
title: T-01–T-04. Observations on build b17
status: stable
sources:
  - resource: requirement.md
  - resource: decision.md
---

# T-01–T-04. Extract from the test log

The tester checked build **b17** on the integration test bench. Before each observation the tester waited for the message to be processed and refreshed the card as the customer. The values in the “Observation” column were taken from the screen of this build. The expectations are set in [R-01, version 2](requirement.md).

| Check and criterion | Action on the test bench | Tester's observation |
|---|---|---|
| T-01 · R-01.1, R-01.3 | Opened order Z-17 with line L1 for 10 units and no shipments. Then sent delivery M-11 with a posted line of document SH-41, L1, 6 units. | First L1 “Shipped 0, remaining 10”, order “Awaiting shipment”. After M-11, “Shipped 6, remaining 4”, “Partially shipped”. |
| T-02 · R-01.2, R-01.3 | For the same order, repeated SH-41/L1 as a separate delivery M-12. The log confirmed processing of M-11 and M-12. | L1 “Shipped 6, remaining 4”, state “Partially shipped”. |
| T-03 · R-01.1, R-01.3, R-01.4 | Added delivery M-13 for Z-17 with a new posted document SH-42, L1, 4 units. The accounting closed flag is not set. | L1 “Shipped 10, remaining 0”. The screen shows “Shipped” in the shipping state and “Open” in the accounting status at the same time. |
| T-04 · R-01.1–R-01.3 | Opened a separate order Z-18. L1 has 2 units ordered, L2 has 3. Sent one posted document SH-43 with lines L1 for 2 and L2 for 1. | L1 “Shipped 2, remaining 0”, L2 “Shipped 1, remaining 2”. Order “Partially shipped”. |
