# PawPal+ Project Reflection

## 1. System Design

**Core user actions:**

1. **Add a pet** — The user can register a pet by entering its name, species, and any relevant details (age, breed, special needs). This is the foundation of the app; everything revolves around a specific pet.
2. **Add and edit care tasks** — The user can create care tasks for their pet (e.g., walk, feeding, medication, grooming) with a duration and priority level. They can also update or remove tasks as their pet's needs change.
3. **Generate a daily care plan** — The user can request an automatically generated daily schedule that organizes their tasks based on available time and priority, so they know exactly what to do and when.

**Building blocks (classes):**

1. **Owner** — Represents the pet owner / app user.
   - *Attributes:* name, available_time (minutes per day)
   - *Methods:* add_pet(), remove_pet()

2. **Pet** — Represents a pet belonging to the owner.
   - *Attributes:* name, species, breed, age
   - *Methods:* add_task(), remove_task(), get_tasks()

3. **Task** — A single care activity for a pet.
   - *Attributes:* name, duration (minutes), priority (high/medium/low), category (walk, feeding, meds, grooming, enrichment)
   - *Methods:* mark_complete(), edit()

4. **Scheduler** — Generates a daily care plan from tasks and constraints.
   - *Attributes:* tasks (list), available_time (minutes)
   - *Methods:* generate_plan(), get_explanation()

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The initial UML design includes four classes:
- **Owner** — Stores the user's name and how many minutes they have per day. Responsible for managing a list of pets (add/remove).
- **Pet** — Stores pet details (name, species, breed, age) and holds a list of care tasks. Responsible for adding, removing, and retrieving tasks.
- **Task** — Represents a single care activity with a name, duration, priority, and category. Can be marked complete or edited.
- **Scheduler** — Takes in a list of tasks and the owner's available time, then generates a prioritized daily plan and an explanation of why tasks were ordered that way.

Relationships: Owner owns one-to-many Pets, each Pet has one-to-many Tasks, and the Scheduler operates on a collection of Tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, two changes were made after reviewing the skeleton with AI:
1. **Priority changed from `str` to `IntEnum`** — The original design used plain strings ("high", "medium", "low") for priority, which is error-prone and harder to sort. Switching to an `IntEnum` (HIGH=1, MEDIUM=2, LOW=3) makes the scheduler's sorting logic cleaner and prevents typos.
2. **Added `pet_name` field to Task** — The original Task had no reference to which pet it belonged to. When an owner has multiple pets and tasks are combined into one plan, the schedule needs to show which pet each task is for.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
