# From request to acceptance of a change

Consulting practice of Alexander Polomodov

If agreed work keeps coming back from development, it is worth taking one specific case apart. When did it become clear that participants understood the expected result differently? Could this have been spotted before development? I propose to trace one change with the team from request to acceptance, and then test the new way of working on the next change.

For management decisions I rely on the Project Management Institute (PMI) approaches to stakeholders and risk. From the Rational Unified Process (RUP) I take iteration planning around a material risk. The link between them is a requirement that can be verified. It tells the architect which solution options are acceptable and gives the customer a basis for accepting the result. [PMI project management principles](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/12-project-management-principles.pdf) · [Project planning with RUP, IBM Rational](https://public.dhe.ibm.com/software/rational/web/whitepapers/2003/tp151.pdf)

## What you can order

| Engagement | What the team gets | When the work is done |
| --- | --- | --- |
| Diagnosis of one change | A map of how the work actually went, with waits and rework loops | Participants have confirmed the sequence of events from working materials and chosen a problem to test |
| Requirement and architecture work-through | A scenario, acceptance criteria, a decision record and a plan for testing the risk | The customer's representative has agreed the expected result and the technical lead has defined how to test it |
| Pilot support and hand-over of the practice | An example of an accepted decision with its test result, working templates and a comparison with the original case | The team has worked through the next change on its own and decided which techniques to keep |

## How the review starts

- Who requested the change, for whom, and what result did they consider sufficient?
- At what point was clarification needed? Who could answer, and what did the team do while waiting?
- Which assumption influenced the choice of architecture? What would revisiting the decision cost if the assumption turns out to be wrong?
- What did the customer base acceptance on? Did it match what the team tested?

To start, the customer picks a completed change and shows the task statement, the decision record and the test results. If the decision was only verbal, we reconstruct it with the participants and note what could be confirmed. For the pilot we pick a comparable upcoming change. Participants include a customer representative with the right to accept the result and the specialists who will design, build and test the solution.

## How the pilot runs

1. With the project manager we choose the pilot boundaries, the baseline case and the sign of improvement. We record who will decide if the scope changes.
2. The customer's representative describes the working scenario. The analyst and the tester turn it into an acceptance condition with an observable result. The architect shows which constraint drives the choice of solution and records the basis for the choice.
3. The team tests the risk in an iteration. In the partial shipments example, the architect reproduces a repeat of one warehouse document and the analyst checks what the customer sees after it. I help the project manager connect the experiment's result to the work estimate. The product owner chooses the behaviour; the sponsor accepts the consequences for date and budget.
4. At the pilot review we compare the baseline and the new case on a measure chosen in advance. For example, we count how often a task went back for clarification after development started and check the reasons in the task history. We separately note differences in complexity and team composition that could have affected the comparison.

On the next change, a member of the customer's staff leads the review. I hand over a completed example, context cards, three agent instructions and six test tasks. We go through an answer in which a correct arithmetic expectation can hide missing acceptance evidence. The hand-over is complete when the staff issue the task on their own, spot such an error and know whom to ask for the evidence or the decision. [Example delivery](example.md) · [Team workshop](agent-practice.md)

## About the author

Alexander Polomodov is an engineering leader and consultant based in London. He works with engineering and product teams on how requirements, architecture decisions, plans and acceptance stay connected, and on bringing AI agents into that work with measurable checks. More talks, articles and podcasts are on [polomodov.tech](https://polomodov.tech).

**Get in touch:** [alex@polomodov.tech](mailto:alex@polomodov.tech) · [LinkedIn](https://www.linkedin.com/in/alexanderpolomodov/) · [Telegram](https://t.me/apolomodov). Sessions run remotely or on site, in English or Russian.

Engagements are subject to applicable sanctions and export-control law. I don't work with sanctioned persons or with organisations where such work is restricted.
