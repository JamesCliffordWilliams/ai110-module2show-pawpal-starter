"""Simple test script for PawPal+ scheduling."""

from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    owner = Owner()

    # Create pets
    rover = Pet(
        pet_name="Rover",
        species="Dog",
        dob=date(2020, 5, 12),
        breed="Labrador",
        medications=["Heartworm"],
    )

    whiskers = Pet(
        pet_name="Whiskers",
        species="Cat",
        dob=date(2019, 9, 3),
        breed="Siamese",
        medications=["Flea"],
    )

    owner.add_pet(rover)
    owner.add_pet(whiskers)

    # Create tasks
    task1 = Task(task_name="Morning walk", duration=30, priority=10, frequency="daily")
    task2 = Task(task_name="Medication", duration=5, priority=100, frequency="daily")
    task3 = Task(task_name="Play session", duration=20, priority=5, frequency="daily")

    # Assign tasks to pets
    rover.add_task(task1)
    rover.add_task(task2)
    whiskers.add_task(task3)

    # Generate and display schedule
    plan = Scheduler.generate_daily_plan(owner, start_time="08:00")

    print("Today's Schedule")
    print("================")

    schedule = plan.get_daily_schedule()
    scheduled_times = schedule.get("scheduled_times", {})

    for task_name, time_slot in scheduled_times.items():
        print(f"{time_slot} - {task_name}")


if __name__ == "__main__":
    main()
