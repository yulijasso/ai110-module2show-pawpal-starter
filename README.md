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

## Smarter Scheduling

PawPal+ includes four algorithmic features that make the scheduler more intelligent:

- **Sort by time** — Tasks with a scheduled time (e.g., 07:00) are placed first in chronological order. Unscheduled tasks follow, sorted by priority then duration. Uses `sorted()` with a lambda key for clean, readable sorting.
- **Filter by pet or status** — `filter_tasks()` lets you view tasks for a specific pet, only incomplete tasks, only completed tasks, or any combination. Useful in both the CLI demo and the Streamlit UI.
- **Recurring tasks** — Tasks can be set to `"daily"` or `"weekly"` recurrence. When a recurring task is marked complete, a new instance is automatically created with the next due date calculated using Python's `timedelta`. Future-dated tasks are excluded from today's schedule until their day arrives.
- **Conflict detection** — The scheduler checks every pair of scheduled tasks for overlapping time windows and labels each conflict as `SAME-PET` (physically impossible) or `CROSS-PET` (may need coordination). Warnings are displayed without crashing the program, so the owner stays in control.

## Testing PawPal+

Run the full test suite with:

```bash
python -m pytest tests/test_pawpal.py -v
```

The suite includes **18 automated tests** organized into five categories:

| Category | Tests | What they verify |
|----------|-------|------------------|
| Schedule generation | 2 | Tasks are sorted by scheduled time first, then by priority/duration. Only tasks within the time budget are included. |
| Recurring tasks | 3 | Daily completion creates a task due tomorrow (+1 day). Weekly creates one due next week (+7 days). Non-recurring tasks produce no new instance. |
| Conflict detection | 3 | Same-pet overlaps produce a SAME-PET warning. Cross-pet overlaps produce a CROSS-PET warning. Non-overlapping tasks produce zero conflicts. |
| Filtering | 3 | Filter by pet name, by completion status, or both combined. |
| Edge cases | 7 | No pets, no tasks, zero available time, task too long, future-dated recurring task, all tasks completed, two tasks at exact same time. |

**Confidence Level: 4/5 stars**

The test suite covers all core scheduling behaviors, both happy paths and edge cases. The one star deducted is because the tests do not yet cover the Streamlit UI layer (app.py) or multi-day scheduling scenarios where recurring tasks chain across several days.

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
