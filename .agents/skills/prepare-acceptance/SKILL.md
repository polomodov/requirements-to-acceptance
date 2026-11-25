---
name: prepare-acceptance
description: Prepares acceptance scenarios from the requirement version in force and matches them against test-run results. Use to write checks or to review evidence before an acceptance decision.
---

# Prepare acceptance

Find the agreed outcome, conditions and exclusions for the specific delivery. Give the requirement ID and version, the decision record and the object under test. For a disputed rule, state explicitly who has to define the expected outcome.

1. For each criterion, set the initial state, the data, the action and the observable result. Pick a normal scenario and an edge case that separates a correct implementation from a plausible mistake. For partial shipments per line, two consecutive shipments and a repeated delivery of the same confirmation are telling. If the repeat rule is still under discussion, record the question and propose a check for approval.
2. For a scenario driven by a sequence of events, give the intermediate states. Match every input to the event status, the line and the operation ID where they determine the outcome. Say exactly where the user or the tester will see the result. Checking data in the accounting system and checking what the portal displays give different evidence.
3. If test-run results are attached, link each to a criterion, the build tested and an observation. Mark confirmed criteria, discrepancies and gaps separately. A demo of the first shipment does not confirm that repeats are handled correctly, and one successful example does not cover the other conditions. Mark a missing observation as untested. For material from another build, say what would justify carrying the evidence over, or which scenario must be repeated.

**Output for acceptance.** Give the tester a table of “criterion / action / expected / observation and source / conclusion”. Without a test run the table remains a plan. If there is a gap, name the missing evidence and who is responsible for obtaining it. Record the authorised owner's acceptance decision with a reference to the record and the scope they accepted.
