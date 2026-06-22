import pytest
from datetime import date, timedelta

from pawpal_system import DailyPlan, Pet, Scheduler, Task


def test_task_mark_complete_sets_completed_status_true() -> None:
    task = Task(task_name="Test Task", duration=10, priority=1)
    assert task.completed_status is False

    task.mark_complete()

    assert task.completed_status is True


def test_pet_add_task_increases_task_count() -> None:
    pet = Pet(
        pet_name="Test Pet",
        species="Dog",
        dob=date(2023, 1, 1),
        breed="Mixed",
    )
    initial_task_count = len(pet.get_tasks())

    task = Task(task_name="Feed", duration=5, priority=1)
    pet.add_task(task)

    assert len(pet.get_tasks()) == initial_task_count + 1


def test_scheduler_sort_by_time_returns_tasks_in_chronological_order() -> None:
    task1 = Task(task_name="Task A", duration=10, priority=1)
    task2 = Task(task_name="Task B", duration=10, priority=1)
    task3 = Task(task_name="Task C", duration=10, priority=1)
    tasks = [task1, task2, task3]
    scheduled_times = {"Task A": "10:00", "Task B": "08:00", "Task C": "09:00"}

    sorted_tasks = Scheduler.sort_by_time(tasks, scheduled_times)

    assert [t.task_name for t in sorted_tasks] == ["Task B", "Task C", "Task A"]


def test_pet_mark_task_complete_creates_recurring_daily_task() -> None:
    pet = Pet(
        pet_name="Test Pet",
        species="Dog",
        dob=date(2023, 1, 1),
        breed="Mixed",
    )
    today = date.today()
    task = Task(task_name="Daily Walk", duration=30, priority=5, frequency="daily", due_date=today)
    pet.add_task(task)

    initial_count = len(pet.get_tasks())
    pet.mark_task_complete("Daily Walk")

    assert len(pet.get_tasks()) == initial_count + 1
    new_task = pet.get_tasks()[-1]
    assert new_task.task_name == "Daily Walk"
    assert new_task.due_date == today + timedelta(days=1)


def test_daily_plan_generate_plan_detects_conflict_and_returns_warning() -> None:
    plan = DailyPlan()
    task1 = Task(task_name="Task 1", duration=0, priority=1)
    task2 = Task(task_name="Task 2", duration=0, priority=1)
    plan.add_task(task1)
    plan.add_task(task2)

    _, warning = plan.generate_plan(start_time="08:00")

    assert warning is not None
    assert "conflict" in warning.lower()

