# Grammar-to-Scenario Framework

## Scenario necessity test

A strong scenario passes all four questions:

1. Would the learner still need the target grammar if the decorative theme were removed?
2. Does the situation contain a cue that makes the target meaning necessary?
3. Can learners explain why one form fits and another does not?
4. Does the final mission require the grammar to communicate successfully?

If the answer to any question is no, redesign the situation before adding more activities.

## Match the visual model to the grammar meaning

| Grammar target | Meaning learners must see | Useful scenario | Visual/interactive model | Possible final output |
| --- | --- | --- | --- | --- |
| `am/is/are → was/were` | now versus finished past time | Recover a memory, investigate yesterday | Reversible Today–Yesterday timeline using the same scene | Past weather report, witness statement, memory story |
| Present continuous | action happening at this moment | Live control room, wildlife camera, video call | Live camera frames; now indicator; action updates | Live commentary |
| Simple present vs present continuous | routine versus temporary action now | School newsroom comparing a normal day with today | Split calendar/live feed | “Usually…, but today…” report |
| Past simple | completed event sequence | Lost-object investigation, trip reconstruction | Evidence timeline; before/after states | Case summary or travel diary |
| `can/can't` | ability, possibility, or permission | Rescue team, talent agency, access checkpoint | Capability scanner or access gate | Recommend a team member; explain permission |
| `there is/are` | existence and number in a place | Design a room, inspect a campsite, map a town | Searchable map or inventory overlay | Location briefing |
| Comparatives | choose by comparing two items on one dimension | Travel planner, product lab, animal research station | Side-by-side comparison scanner with one changing measure | Recommendation with reasons |
| Superlatives | select the extreme in a group | Awards panel, expedition planning | Ranked field or podium | Announce and justify a winner |
| `some/any` | presence, absence, offer, or request | Café stockroom, picnic planner, supply mission | Inventory with positive, negative, and question states | Shopping or supply dialogue |
| `much/many` | quantity type and amount | Waste audit, market survey | Two quantity meters for count and mass | Data report |
| `should/shouldn't` | advice based on a problem | Help desk, school clinic, travel safety desk | Problem-to-advice decision board | Advice message |
| `must/have to` | obligation from rule or circumstance | Space station rules, museum security, camp safety | Rule scanner and consequence path | Safety briefing |
| `going to` | prior intention or evidence-based prediction | Event planner, weather emergency desk | Plan board or evidence forecast | Plan/prediction briefing |
| `will` | decision, offer, promise, or prediction | Community response centre | Incoming problem and instant-response console | Promise or response plan |
| First conditional | likely condition and result | Eco mission, safety simulator | Branching “if → result” path | Action plan |
| Present perfect | past experience connected to now | Explorer passport, achievement archive | Experience stamps without finished-time labels | Interview about experiences |

This table suggests logic, not fixed themes. Prefer a scenario that fits the user's material, learners, and classroom culture.

## Build the contrast before the rule

Hold vocabulary and scene constant while changing the grammatical meaning.

Examples:

- Time: `It is sunny.` ↔ `It was sunny.`
- Routine/now: `She reads after school.` ↔ `She is reading now.`
- Existence/number: `There is a tent.` ↔ `There are three tents.`
- Ability: `The robot can lift the box.` ↔ `The small robot can't lift it.`
- Comparison: `Train A is fast.` ↔ `Train B is faster.`

Only after learners notice the meaning change should the page summarize the form.

## Turn practice into communication

Replace isolated selection with a purpose:

- **Evidence:** choose a form because a clue establishes time, number, intention, or obligation.
- **Information gap:** one learner has facts another needs.
- **Decision:** compare options and recommend one.
- **Repair:** correct a message so a plan can continue.
- **Prediction:** use visible evidence to state what will happen.
- **Final product:** broadcast, briefing, interview, advice note, plan, map description, or case report.

## Reject these weak patterns

- A vocabulary-card grid renamed as a “map,” “lab,” or “mission.”
- A timeline that lists events but never compares present and past meaning.
- A race, timer, or score that rewards speed without requiring target-language reasoning.
- A story theme that could be swapped without changing any grammar decision.
- A final task that asks learners to repeat the model without choosing their own content.
- Long grammar terminology before learners encounter the communicative problem.

## Technical structure markers

Use these invisible attributes in generated HTML:

```html
<body data-lesson-mode="grammar-scenario" data-grammar-target="present-continuous">
  <section data-stage="context">...</section>
  <section data-stage="meaning">...</section>
  <section data-stage="pattern-discovery">...</section>
  <section data-stage="application">...</section>
  <section data-stage="output">...</section>
</body>
```

Additional stages such as guided practice, investigation, rehearsal, or reflection are welcome. Visible module titles should belong to the scenario rather than repeat these internal markers.
