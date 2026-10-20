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

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```
Today's Schedule
----------------
08:00 - Mochi: Breakfast (10 min) [high]
12:00 - Luna: Medication (5 min) [high]
18:00 - Mochi: Evening walk (30 min) [high]



## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```
rootdir: C:\Users\giang\Codepath\ai110-module2show-pawpal-starter        
plugins: anyio-4.15.1
collected 7 items                                                       

tests\test_pawpal.py .......                                      [100%] 

========================== 7 passed in 0.04s =========================== 
## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.
## Smarter Scheduling

| Feature | Method | Behavior |
|---|---|---|
| Sorting | `Scheduler.sort_by_time()` | Sorts all pets' tasks by HH:MM time |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet or completion status |
| Recurrence | `Scheduler.mark_task_complete()` | Creates the next daily or weekly occurrence |
| Conflict detection | `Scheduler.find_conflicts()` | Detects tasks scheduled for the same date and time |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. The user starts PawPal+ and enters their pet information.
2. The user adds Mochi, a dog, and Luna, a cat.
3. The user schedules tasks such as feeding, medication, and walks.
4. PawPal+ retrieves tasks for all pets through the Owner object.
5. The Scheduler sorts tasks chronologically.
6. Daily or weekly tasks automatically create their next occurrence after completion.
7. Tasks scheduled for the same date and time are identified as conflicts.
8. The same scheduling behavior can be verified with the CLI demo by running:

```bash
python main.py

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
