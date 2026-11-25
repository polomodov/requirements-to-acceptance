---
type: Requirement
title: R-01. Shipping state and quantities per line. Version 2
status: stable
sources:
  - resource: intake.md
  - resource: prototype.md
  - resource: decision.md
---

# R-01. Order card, version 2

The product owner approved the behaviour on 7 October 2026 for the delivery with acceptance on 21 October. The business analyst issued this version after both approvals in D-01. The accounting status from version 1 keeps its original source. [Original version](intake.md) · [Basis for the change](decision.md)

| Criterion | Observable behaviour after the data is processed and the card is refreshed |
|---|---|
| R-01.1. Remainder per line | For each line show “Shipped”, the number of units shipped, and “Remaining”, the difference between ordered and shipped. Before the first shipment, on a line for 10 units the customer sees “Shipped 0, remaining 10”. After 6 units ship, “Shipped 6, remaining 4”. |
| R-01.2. Repeats and multiple lines | Within one warehouse and order, count each posted immutable record once by the “shipment number + order line” pair. When the same pair is delivered again, quantities and state stay the same. Two different lines of one document are each counted against their own order line. |
| R-01.3. Order shipping state | Before the first shipment show “Awaiting shipment”. If at least one unit has shipped and any line has a remainder, show “Partially shipped”. When every line has shipped in full, show “Shipped”. |
| R-01.4. Accounting status | Show “Open” or “Closed” separately, based on the order's closed flag in the accounting system. When everything has shipped and the closed flag is not set, the customer sees “Shipped” and “Open” at the same time. |

**Delivery boundary.** One warehouse, posted immutable records for the order. The date of the next truck, returns, reversals and cancellations are outside this version.

**Linked work.** Package 1.1 is the scenario and the data check, 1.2 the customer screen, 1.3 matching and counting of lines, 1.4 testing and presenting the build. The basis for the de-duplication key is kept in [E-01](prototype.md).
