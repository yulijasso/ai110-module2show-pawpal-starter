from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    name: str
    duration: int  # minutes
    priority: str  # "high", "medium", "low"
    category: str  # "walk", "feeding", "meds", "grooming", "enrichment"
    completed: bool = False

    def mark_complete(self):
        pass

    def edit(self, name=None, duration=None, priority=None, category=None):
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str = ""
    age: int = 0
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass


@dataclass
class Owner:
    name: str
    available_time: int  # minutes per day
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass


class Scheduler:
    def __init__(self, tasks: List[Task], available_time: int):
        self.tasks = tasks
        self.available_time = available_time

    def generate_plan(self) -> List[Task]:
        pass

    def get_explanation(self) -> str:
        pass
