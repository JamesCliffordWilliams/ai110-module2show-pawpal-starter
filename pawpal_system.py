from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional


@dataclass
class Pet:
    pet_name: str
    species: str
    dob: date
    breed: str
    medications: List[str] = field(default_factory=list)

    def get_pet_info(self) -> Dict[str, object]:
        """Return pet profile information."""
        pass

    def update_pet_info(self, **kwargs) -> None:
        """Update pet attributes based on provided keyword arguments."""
        pass

    def get_age(self) -> int:
        """Return the pet's age in years."""
        pass


class User:
    def __init__(
        self,
        unavailable_times: Optional[List[str]] = None,
        preferences: Optional[Dict[str, object]] = None,
        priorities: Optional[Dict[str, object]] = None,
    ):
        self.unavailable_times = unavailable_times or []
        self.preferences = preferences or {}
        self.priorities = priorities or {}

    def get_user_info(self) -> Dict[str, object]:
        """Return user profile and preference information."""
        pass

    def update_preferences(self, **kwargs) -> None:
        """Update user preferences."""
        pass

    def add_unavailable_time(self, time_slot: str) -> None:
        """Mark a time slot as unavailable."""
        pass


@dataclass
class Task:
    task_name: str
    duration: int
    priority: int
    completed_status: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        pass

    def update_priority(self, priority: int) -> None:
        """Update the priority level of the task."""
        pass

    def update_duration(self, duration: int) -> None:
        """Update the expected duration of the task."""
        pass

    def get_task_info(self) -> Dict[str, object]:
        """Return task details."""
        pass


class DailyPlan:
    def __init__(
        self,
        tasks: Optional[List[Task]] = None,
        scheduled_times: Optional[Dict[str, str]] = None,
        daily_constraints: Optional[Dict[str, object]] = None,
    ):
        self.tasks = tasks or []
        self.scheduled_times = scheduled_times or {}
        self.daily_constraints = daily_constraints or {}

    def add_task(self, task: Task) -> None:
        """Add a task to the daily plan."""
        pass

    def generate_plan(self) -> None:
        """Generate a schedule for the day based on tasks and constraints."""
        pass

    def get_daily_schedule(self) -> Dict[str, object]:
        """Return the current daily schedule."""
        pass

    def update_schedule(self, scheduled_times: Dict[str, str]) -> None:
        """Update the scheduled times for the day."""
        pass
