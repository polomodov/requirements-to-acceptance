---
type: Decision
title: D-01. Partial shipment scope and plan change
status: stable
sources:
  - resource: intake.md
  - resource: prototype.md
---

# D-01. Decision record, 7 October 2026

**Subject.** The accounting status from R-01, version 1, stays on the order card. The team considered two ways to tell the customer how shipping is going. The log field check and the activity estimates are attached to the decision. [I-01 and I-02](intake.md) · [E-01 and the estimate sheet](prototype.md)

| Option | What the customer sees after 6 of 10 have shipped | Product owner's conclusion |
|---|---|---|
| A. First-shipment marker | Sees that shipping has started. Asks the account manager for the remainder. | A general marker leaves the customer's second question open. |
| B. Quantities per line | On the order line sees 6 shipped and 4 remaining. On the order sees the shipping state. | The option answers both enquiries and lets each line be checked. |

**Scope approval.** On 7 October the product owner chose B for this delivery. In scope: posted, immutable shipment lines from one warehouse, repeated delivery, quantities per line and the overall shipping state. The date of the next truck remains an open request from sales. Returns, reversals and cancellations are outside the delivery.

| Project manager's calculation | Baseline before D-01 | Option B | Change |
|---|---:|---:|---:|
| Effort | 13 person-days | 19 person-days | +6 person-days |
| Labour budget | 6,500 euros | 9,500 euros | +3,000 euros |
| Critical path A–B–D–E–F | 10 working days | 13 working days | +3 working days |
| Acceptance date | 16 October | 21 October | +3 working days |

**Approval of commitments.** On 7 October the sponsor approved, for option B, a labour budget of 9,500 euros and an acceptance date of 21 October 2026. The updated baseline is in force from this decision. In it C finishes on 13 October, D on 15 October and E on 20 October. The screen work has two working days of float before D finishes. The project manager reflected the changes in packages 1.2, 1.3 and 1.4. The business analyst issued [R-01, version 2](requirement.md).
