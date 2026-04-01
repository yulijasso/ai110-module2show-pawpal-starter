from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional


class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


@dataclass
class Task:
    name: str
    duration: int  # minutes
    priority: Priority
    category: str  # "walk", "feeding", "meds", "grooming", "enrichment"
    pet_name: str = ""
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def edit(
        self,
        name: Optional[str] = None,
        duration: Optional[int] = None,
        priority: Optional[Priority] = None,
        category: Optional[str] = None,
    ):
        """Update one or more task fields."""
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        if priority is not None:
            self.priority = priority
        if category is not None:
            self.category = category


@dataclass
class Pet:
    name: str
    species: str
    breed: str = ""
    age: int = 0
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet and stamp it with the pet's name."""
        task.pet_name = self.name
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet's task list."""
        self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return a copy of this pet's task list."""
        return list(self.tasks)


@dataclass
class Owner:
    name: str
    available_time: int  # minutes per day
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner's pet list."""
        self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        """Collect and return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def generate_plan(self) -> List[Task]:
        """Build a prioritized daily plan that fits within the owner's available time."""
        tasks = [t for t in self.owner.get_all_tasks() if not t.completed]
        # Sort by priority (HIGH=1 first), then by duration (shorter first)
        tasks.sort(key=lambda t: (t.priority, t.duration))

        plan = []
        remaining_time = self.owner.available_time
        for task in tasks:
            if task.duration <= remaining_time:
                plan.append(task)
                remaining_time -= task.duration
        return plan

    def get_explanation(self) -> str:
        """Return a human-readable summary of the daily plan with reasoning."""
        plan = self.generate_plan()
        if not plan:
            return "No tasks could be scheduled. Check your available time or add tasks."

        total_time = sum(t.duration for t in plan)
        lines = [
            f"Daily plan for {self.owner.name} "
            f"({total_time}/{self.owner.available_time} minutes used):",
            "",
        ]
        for i, task in enumerate(plan, start=1):
            lines.append(
                f"  {i}. [{task.priority.name}] {task.name} "
                f"({task.pet_name}) - {task.duration} min"
            )

        skipped = [t for t in self.owner.get_all_tasks()
                    if not t.completed and t not in plan]
        if skipped:
            lines.append("")
            lines.append("Skipped (not enough time):")
            for task in skipped:
                lines.append(
                    f"  - {task.name} ({task.pet_name}) - {task.duration} min"
                )

        lines.append("")
        lines.append(
            "Tasks are ordered by priority (high first), "
            "then by duration (shorter first) to fit as many as possible."
        )
        return "\n".join(lines)
