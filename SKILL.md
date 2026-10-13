---
name: grammar-scenario-lesson
description: Create or revise self-contained interactive English grammar lesson websites in which a meaningful scenario makes the target form necessary. Use for scenario-based grammar pages, role-driven grammar courseware, or requests to teach the use and reason behind structures such as was/were, present continuous, can/can't, there is/are, comparatives, modals, or future forms. Do not use for vocabulary-only pages or ordinary printable worksheets.
---

# Grammar Scenario Lesson

Create an offline interactive lesson that answers two learner questions before drilling form:

1. **What does this grammar help me mean or do?**
2. **Why is this form necessary in this situation?**

The scenario is not decoration. It must create the communicative need for the target grammar.

## Inputs and inference

Identify the target grammar, learner level, and any requested topic or source material. If the user gives only a grammar point, infer an age-appropriate scenario from its communicative function instead of asking for a theme. Read [references/grammar-to-scenario-framework.md](references/grammar-to-scenario-framework.md) before designing a new scenario.

Use [assets/worked-example-weather-was-were.html](assets/worked-example-weather-was-were.html) only as a worked example of quality and logic. Do not copy its weather setting, role names, module names, or seven-part structure unless they genuinely fit the new grammar target.

## Design the lesson spine

Before writing the page, determine:

- **Meaning:** the idea or relationship expressed by the grammar.
- **Trigger:** the time signal, situation, speaker goal, or evidence that makes the form necessary.
- **Contrast:** two closely matched situations that isolate the grammar change.
- **Misconception:** what learners commonly know as a rule but fail to apply.
- **Communicative job:** what learners will accomplish with the grammar in the final task.

Choose a scenario with a learner identity, a goal, an information gap or decision, and a visible outcome. Use vocabulary as evidence and content inside the scenario, not as a separate flashcard lesson.

## Build a meaning-first arc

Adapt the number and names of modules to the grammar and scenario. Preserve this learning progression:

1. **Enter the situation:** observe a world, problem, message, map, schedule, case, or mission.
2. **See the meaning contrast:** keep most of the scene constant and change only the dimension controlled by the grammar.
3. **Discover the pattern:** let learners notice how meaning maps to form before giving a compact rule.
4. **Use the grammar as a tool:** solve evidence, make a choice, repair communication, or obtain missing information.
5. **Rehearse output:** provide a model, sentence frame, and supported interaction.
6. **Complete an authentic mission:** speak or write to achieve the scenario goal.

Give modules immersive names tied to the scenario. Avoid headings such as “Vocabulary,” “Grammar Explanation,” “Quiz,” or “Team Relay” unless the user explicitly requests conventional courseware.

## Interaction requirements

- Choose a visual metaphor that matches the grammar meaning: a timeline for past time, a live camera for actions happening now, a comparison scanner for comparatives, an inventory or map for `there is/are`, an access gate for ability or permission, or a planner for future intention.
- The central contrast must remain simultaneously visible or easily reversible so learners can compare meaning, not memorize an isolated rule.
- Every major interaction must require noticing, choosing, interpreting, or producing the target language. Remove mechanics that could be completed without using the grammar.
- Include immediate feedback, answer reveal, a model output, speech support when useful, keyboard focus, responsive layout, and a global reset.
- Provide at least one guided output and one independent scenario-ending output. Pair or group interaction is recommended when it creates real information exchange.
- Keep the finished page self-contained: one HTML file with inline CSS and JavaScript and no required network assets.
- Mark the document body with `data-lesson-mode="grammar-scenario"` and a concise `data-grammar-target`. Mark the main stages with `data-stage="context"`, `meaning`, `pattern-discovery`, `application`, and `output` so the structure can be validated without controlling visible headings.

## Content integrity

- Keep language appropriate to the stated CEFR level and age.
- Make stored answers, visible options, feedback, speech text, model output, and reset defaults agree.
- Use short Chinese support only when it clarifies why the structure is needed.
- Avoid ambiguous distractors, fake communication, and examples whose context does not justify the target form.
- Preserve user-provided content and visual choices unless they conflict with the requested revision.

## Validate and deliver

Resolve this skill folder, then run:

```bash
python3 <skill-root>/scripts/validate_grammar_scenario.py /absolute/path/to/lesson.html
```

Fix every reported error. Package the final HTML in a ZIP and return clickable absolute links to both files. Briefly explain the scenario, the grammar function it makes visible, and the final learner output.
