---
name: trace-change-impact
description: Prepares an impact assessment of a requirement change through its links to architecture, tests, work packages, schedule and cost. Use to analyse a solution option or to recalculate a delivery plan.
---

# Assess the impact of a change

Establish which version of the scope, schedule and budget the option is being compared against. From the OKF cards or the records provided, find out who requested the change and whether there is a decision on behaviour, date and budget. Tie each approval to its source and to the scope of the approver's authority.

1. Trace from the changed rule to the affected elements. For each, give the specific change or the reason to re-check it, the owner and the basis of the link. When remaining quantity per order line is requested, find out whether confirmed quantities are available for every line. The exchange contract, the data model, the portal screen and the acceptance scenario may all depend on that. Carry a prototype result over only to the conditions it actually tested.
2. Show which deliverable is added or changed in the work breakdown structure (WBS) and which activities will produce it. Find dependencies and shared work so that one integration change is not counted twice in the estimate. Include activities outside the changed branch in the schedule recalculation if the finish date depends on them.
3. When durations and dependencies are known, calculate the original and the changed network. If an activity starts after several predecessors finish, its early start is set by the latest of their finish dates. Take into account the working calendar, lags between activities and the availability of people, if given. Show the critical path and the milestone shift. Sum effort separately and calculate labour cost at the corresponding rates. If data is missing, give the part of the calculation you can and a targeted request for the missing value.

**Output for the decision.** Present the original and the proposed state, the difference, the assumptions and the links that owners still need to check. State clearly which plan is in force, what is a forecast and which commitments have already been approved. The product owner's agreement on behaviour extends to date or cost only where they are confirmed to have authority over those.
