# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Features

PawPal+ includes several smart algorithms to make pet care planning easier:

- **Sorting tasks by time**: Automatically orders tasks by their scheduled "HH:MM" time for a clear daily view.
- **Filtering tasks**: Lets you filter tasks by completion status or by specific pet.
- **Recurring tasks**: Handles daily or weekly tasks by automatically creating new instances when you mark them complete.
- **Conflict detection**: Warns if two tasks are scheduled at the same time to avoid overlaps.

## Testing PawPal+

Run the tests with `python3 -m pytest` to check that everything's working.

The tests cover sorting tasks by time to make sure they come out in the right order, handling recurring tasks like daily walks, and spotting conflicts when tasks overlap.

Confidence Level: ⭐⭐⭐⭐ (Pretty solid, but could use more edge case tests.)
