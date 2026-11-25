---
name: clarify-requirement
description: Helps a business analyst turn a request or a dispute about product behaviour into a testable requirement. Use when working through interviews, correspondence and conflicting versions of a requirement.
---

# Clarify a requirement

Start with the delivery and the question to be settled. In the materials provided or in the OKF cards, find the rule currently in force, the original statement and the record of who holds authority. Next to every material claim, give the source, its version and the exact location. If the primary source is not available, mark whose retelling the conclusion rests on.

1. Describe one observable scenario. Who acts, which object changes, on which event, and what will the user see? For partial shipments, distinguish the order, the order line and the shipment. Find out which event records that a shipment has actually happened and at what level of detail it arrives. A message that goods are being prepared and a confirmation of hand-over can mean different things.
2. Compare the statements on the same input data. If they require different outcomes under the same conditions, show both outcomes and the source of each. If the delivery, the user role or the conditions differ, say whether the rules can coexist. Call out a technical constraint separately. For example, a single order-closed flag cannot tell you the shipped quantity on each line.
3. To support the choice, offer options with observable behaviour and a check that tells one from the other. Say which question goes to the product owner and which assumption the architect will test. If the materials contain no decision by an authorised person, keep the version in force and state the status of the new wording. A late remark or a successful prototype does not amount to such a decision on its own.

**Output for the team.** Give the business analyst a card with the sources, the version in force, the proposed rule and an example check. Phrase the open question so that its answer determines how the product will behave. If a decision has already been made, attach its basis, effective date and the scope the approval covers. For a new artefact, use the project's own naming conventions.
