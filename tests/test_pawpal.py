import pytest
from datetime import date

from pawpal_system import Pet, Task


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
