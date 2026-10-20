from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    """Represent one pet-care activity."""
    description: str
    time: str
    duration_minutes: int
    priority: str = "medium"
    frequency: str = "once"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represent a pet and its care tasks."""
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a care task to this pet."""
        self.tasks.append(task)


class Owner:
    """Represent a pet owner who may have multiple pets."""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return tasks from every pet with the associated pet."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))

        return all_tasks


class Scheduler:
    """Organize and manage care tasks for an owner."""

    def __init__(self, owner):
        self.owner = owner

    def sort_by_time(self):
        """Return every task sorted chronologically by HH:MM time."""
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda item: item[1].time
        )

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name and/or completion status."""
        result = []

        for pet, task in self.owner.get_all_tasks():

            if pet_name is not None and pet.name != pet_name:
                continue

            if completed is not None and task.completed != completed:
                continue

            result.append((pet, task))

        return result

    def mark_task_complete(self, pet_name, task_index):
        """
        Complete one task and create the next occurrence
        when the task is daily or weekly.
        """
        pet = None

        for current_pet in self.owner.pets:
            if current_pet.name == pet_name:
                pet = current_pet
                break

        if pet is None:
            return None

        if task_index < 0 or task_index >= len(pet.tasks):
            return None

        task = pet.tasks[task_index]
        task.mark_complete()

        if task.frequency == "daily":
            next_date = task.due_date + timedelta(days=1)

        elif task.frequency == "weekly":
            next_date = task.due_date + timedelta(days=7)

        else:
            return None

        new_task = Task(
            description=task.description,
            time=task.time,
            duration_minutes=task.duration_minutes,
            priority=task.priority,
            frequency=task.frequency,
            due_date=next_date
        )

        pet.add_task(new_task)

        return new_task

    def find_conflicts(self):
        """Return task pairs scheduled for the same date and time."""
        tasks = self.owner.get_all_tasks()
        conflicts = []

        for i in range(len(tasks)):
            pet1, task1 = tasks[i]

            for j in range(i + 1, len(tasks)):
                pet2, task2 = tasks[j]

                if (
                    task1.due_date == task2.due_date
                    and task1.time == task2.time
                    and not task1.completed
                    and not task2.completed
                ):
                    conflicts.append(
                        ((pet1, task1), (pet2, task2))
                    )

        return conflicts