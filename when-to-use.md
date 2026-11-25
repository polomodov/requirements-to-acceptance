# When to use the method

## Where decisions drift apart

A small change was agreed at a meeting. The developer has already built it into the product, the tester is checking the previous version, and the project manager is promising delivery on the original estimate. Each of them acts sensibly within their own document. The problem only becomes visible when the three documents are compared.

The method helps the team reach one shared decision earlier: which behaviour goes into a specific delivery, how the team will verify it, and which commitments on work, dates and cost follow from that choice. It is aimed at the project manager, the product owner and the architect, who are jointly responsible for the result but make different decisions.

## When this work pays off

| What the team notices | How to check whether the method is needed |
|---|---|
| At acceptance, people argue about an exception that was discussed long ago. | Ask the analyst and the tester to name, independently, the rule in force, its version and its basis. The discrepancy shows which link needs to be restored. |
| An estimate was given although the way to implement it has not been tested yet. | Ask the architect to name the assumption whose failure would change the estimate most, and the project manager to show the corresponding work or float in the plan. |
| A small change moved the promised date, and participants explain it differently. | Find the affected deliverable, its dependencies, the assignee's workload and the nearest acceptance window. If the link has to be reconstructed verbally every time, it needs an owner. |

For a small team, one card and a link to a ticket with an acceptance criterion are enough. Add detail where the cost of a mistake justifies the extra effort: an external deadline, expensive rework, several decision owners or a dependency on another team.

## The core of the approach

PMI practices help the project manager agree the result and the boundaries of the work, assign responsibility and assess the consequences of a choice. The Rational Unified Process (RUP) provides the engineering rhythm: in each iteration the team tests a material uncertainty and presents a result on which the next decision can be made. What connects the two is a requirement version tied to a specific delivery. From it you can find the architectural rationale, the test result, the work package and the decision in force.

The trace works in both directions. From a revised requirement the manager reaches the affected milestone. From a finished feature the acceptor goes back to the criterion, the requirement version and the person who confirmed the required result. If the chain breaks, the team sees a specific question to decide. The proposed way of working is the author's own combination of practices and can be used in the team's existing tools.

Next: [the method](method.md) · [the worked example](example.md)
