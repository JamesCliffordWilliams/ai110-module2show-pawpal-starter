from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional


@dataclass
class Task:
    task_name: str
    duration: int  # duration in minutes
    priority: int
    frequency: Optional[str] = None
    completed_status: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed_status = True

    def update_priority(self, priority: int) -> None:
        """Update the priority level of the task."""
        self.priority = priority

    def update_duration(self, duration: int) -> None:
        """Update the expected duration of the task (in minutes)."""
        self.duration = duration

    def get_task_info(self) -> Dict[str, object]:
        """Return a dictionary representation of the task."""
        return {
            "task_name": self.task_name,
            "duration": self.duration,
            "priority": self.priority,
            "frequency": self.frequency,
            "completed_status": self.completed_status,
        }


@dataclass
class Pet:
    pet_name: str
    species: str
    dob: date
    breed: str
    medications: List[str] = field(default_factory=list)
    tasks: List[Task] = field(default_factory=list)

    def get_pet_info(self) -> Dict[str, object]:
        """Return pet profile information."""
        return {
            "pet_name": self.pet_name,
            "species": self.species,
            "dob": self.dob.isoformat(),
            "breed": self.breed,
            "medications": list(self.medications),
            "tasks": [t.get_task_info() for t in self.tasks],
        }

    def update_pet_info(self, **kwargs) -> None:
        """Update pet attributes based on provided keyword arguments."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_age(self) -> int:
        """Return the pet's age in years."""
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task_name: str) -> bool:
        """Remove a task by name. Returns True if removed."""
        for i, task in enumerate(self.tasks):
            if task.task_name == task_name:
                self.tasks.pop(i)
                return True
        return False

    def get_tasks(self) -> List[Task]:
        """Return a list of tasks for this pet."""
        return list(self.tasks)


class User:
    """Represents an owner of one or more pets."""

    def __init__(
        self,
        unavailable_times: Optional[List[str]] = None,
        preferences: Optional[Dict[str, object]] = None,
        priorities: Optional[Dict[str, object]] = None,
        pets: Optional[List[Pet]] = None,
    ):
        """Initialize the owner with optional availability, preferences, and pets."""
        self.unavailable_times = unavailable_times or []
        self.preferences = preferences or {}
        self.priorities = priorities or {}
        self.pets = pets or []

    def get_user_info(self) -> Dict[str, object]:
        """Return user profile and preference information."""
        return {
            "unavailable_times": list(self.unavailable_times),
            "preferences": dict(self.preferences),
            "priorities": dict(self.priorities),
            "pets": [pet.get_pet_info() for pet in self.pets],
        }

    def update_preferences(self, **kwargs) -> None:
        """Update user preferences."""
        self.preferences.update(kwargs)

    def add_unavailable_time(self, time_slot: str) -> None:
        """Mark a time slot as unavailable."""
        if time_slot not in self.unavailable_times:
            self.unavailable_times.append(time_slot)

    def add_pet(self, pet: Pet) -> None:
        """Add a new pet to the owner's collection."""
        if not any(p.pet_name == pet.pet_name for p in self.pets):
            self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> bool:
        """Remove a pet by name. Returns True if removed."""
        for i, pet in enumerate(self.pets):
            if pet.pet_name == pet_name:
                self.pets.pop(i)
                return True
        return False

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        tasks: List[Task] = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks

    def get_tasks_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks for a specific pet."""
        for pet in self.pets:
            if pet.pet_name == pet_name:
                return pet.get_tasks()
        return []


class DailyPlan:
    def __init__(
        self,
        tasks: Optional[List[Task]] = None,
        scheduled_times: Optional[Dict[str, str]] = None,
        daily_constraints: Optional[Dict[str, object]] = None,
    ):
        """Initialize a daily plan with optional tasks and scheduling constraints."""
        self.tasks = tasks or []
        self.scheduled_times = scheduled_times or {}
        self.daily_constraints = daily_constraints or {}

    def add_task(self, task: Task) -> None:
        """Add a task to the daily plan."""
        self.tasks.append(task)

    def generate_plan(self, start_time: str = "08:00") -> None:
        """Generate a schedule for the day based on tasks and constraints."""
        # Simple greedy schedule: sort by priority (higher first), then assign time slots sequentially.
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority, reverse=True)
        current = datetime.strptime(start_time, "%H:%M")
        self.scheduled_times = {}

        for task in sorted_tasks:
            slot = current.strftime("%H:%M")
            self.scheduled_times[task.task_name] = slot
            current += timedelta(minutes=task.duration)

    def get_daily_schedule(self) -> Dict[str, object]:
        """Return the current daily schedule."""
        return {
            "tasks": [t.get_task_info() for t in self.tasks],
            "scheduled_times": dict(self.scheduled_times),
            "daily_constraints": dict(self.daily_constraints),
        }

    def update_schedule(self, scheduled_times: Dict[str, str]) -> None:
        """Update the scheduled times for the day."""
        self.scheduled_times.update(scheduled_times)


class Scheduler:
    """Encapsulates scheduling logic using owner and pet tasks."""

    @staticmethod
    def generate_daily_plan(owner: User, start_time: str = "08:00") -> DailyPlan:
        """Generate a daily plan based on the owner's pets and their tasks."""
        plan = DailyPlan(tasks=owner.get_all_tasks())
        plan.generate_plan(start_time=start_time)
        return plan


# Alias for clarity in domain modeling.
Owner = User
