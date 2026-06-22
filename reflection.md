# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Core actions:

    Users of PawPal+ should be able to:
    1. View a personalized calendar that details when pet care tasks should be completed, this calendar should take into account the users entered information about their current time obligations to prevent scheduling conflicts
    2. Mark tasks as done
    3. Add pets and their information like name, species, dob, breed.

    What are the main objects needed for this system?
    We will need:
    1. A pet object
        This object will store pet_name, species, dob, breed, medications.
        It will include get_pet_info(), update_pet_info(), get_age().

    2. A schedule or daily plan object
        This object will store tasks, scheduled_times, and daily_constraints.
        It will include add_task(), generate_plan(), get_daily_schedule(), update_schedule().

    3. A user object
        This object will store unavailable_times, preferences, and priorities.
        It will include get_user_info(), update_preferences(), add_unavailable_time().

    4. A task object
        This object will store task_name, duration, priority, completed_status.
        It will include mark_complete(), update_priority(), update_duration(), get_task_info().

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four classes: Pet, User, Task, and DailyPlan. The Pet class stores information about the pet like its name, species, breed, date of birth, and medications. The User class represents the owner and keeps track of things like unavailable times and preferences that affect scheduling. The Task class represents individual care tasks such as feeding or walking and stores details like duration, priority, and whether the task is completed. The DailyPlan class is responsible for organizing tasks and generating a schedule for the day based on the user’s constraints and task priorities.

**Updated UML Diagram:**

```mermaid
classDiagram
    class Task {
        +str task_name
        +int duration
        +int priority
        +Optional[str] frequency
        +bool completed_status
        +Optional[date] due_date
        +mark_complete()
        +update_priority(int)
        +update_duration(int)
        +get_task_info() Dict
    }

    class Pet {
        +str pet_name
        +str species
        +date dob
        +str breed
        +List[str] medications
        +List[Task] tasks
        +get_pet_info() Dict
        +update_pet_info(**kwargs)
        +get_age() int
        +add_task(Task)
        +remove_task(str) bool
        +get_tasks() List[Task]
        +mark_task_complete(str) bool
    }

    class User {
        +List[str] unavailable_times
        +Dict preferences
        +Dict priorities
        +List[Pet] pets
        +get_user_info() Dict
        +update_preferences(**kwargs)
        +add_unavailable_time(str)
        +add_pet(Pet)
        +remove_pet(str) bool
        +get_all_tasks() List[Task]
        +get_tasks_by_pet(str) List[Task]
        +filter_tasks(completed=None, pet_name=None) List[Task]
    }

    class DailyPlan {
        +List[Task] tasks
        +Dict scheduled_times
        +Dict daily_constraints
        +add_task(Task)
        +generate_plan(str) Tuple[None, Optional[str]]
        +get_daily_schedule() Dict
        +update_schedule(Dict)
    }

    class Scheduler {
        +sort_by_time(List[Task], Dict) List[Task]
        +generate_daily_plan(User, str) Tuple[DailyPlan, Optional[str]]
    }

    User ||--o{ Pet : owns
    Pet ||--o{ Task : has
    DailyPlan ||--o{ Task : contains
    Scheduler ..> User : uses
    Scheduler ..> DailyPlan : creates

b. Design changes

Did your design change during implementation?

If yes, describe at least one change and why you made it.

Yes, the design changed slightly during implementation. I added a Scheduler class to handle more advanced logic like sorting tasks, detecting conflicts, and generating the daily plan. I also added attributes like frequency and due_date to the Task class so the system could support recurring tasks. These changes helped organize the scheduling logic and kept the responsibilities of each class clearer.

2. Scheduling Logic and Tradeoffs

a. Constraints and priorities

What constraints does your scheduler consider (for example: time, priority, preferences)?

How did you decide which constraints mattered most?

The scheduler mainly considers task priority and time when generating the schedule. Tasks are sorted based on priority and then assigned times starting from the beginning of the day. I focused on priority because some tasks like medication are more important and should be scheduled earlier than lower priority tasks like playtime.

b. Tradeoffs

Describe one tradeoff your scheduler makes.

Why is that tradeoff reasonable for this scenario?

One tradeoff in my scheduler is that it only checks for tasks scheduled at the exact same time to detect conflicts. It does not check for overlapping durations between tasks. This keeps the logic simple and easier to implement, but it means the system might miss cases where one task starts before another one finishes.

This tradeoff is reasonable because the app is meant to be a simple helper for pet owners, not a full scheduling system. Checking exact time matches still catches the most obvious conflicts while keeping the code easier to maintain.

3. AI Collaboration

a. How you used AI

How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

What kinds of prompts or questions were most helpful?

I used Copilot for generating initial class skeletons, implementing method bodies, writing tests, and updating documentation. The most helpful features were code completion for boilerplate and quick fixes for syntax errors. Prompts like "implement this method" or "add tests for these behaviors" worked best.

b. Judgment and verification

Describe one moment where you did not accept an AI suggestion as-is.

How did you evaluate or verify what the AI suggested?

One time, Copilot suggested a more complex way to handle recurring tasks using a separate scheduling structure. I simplified the approach by keeping the recurring logic inside the Pet class instead. I verified that it worked correctly by running my tests and checking that new recurring tasks were created properly.

4. Testing and Verification

a. What you tested

What behaviors did you test?

Why were these tests important?

I tested task completion, task addition, sorting by time, recurring task creation, and conflict detection. These tests were important because they verify that the core scheduling logic works correctly and that the system handles common situations without breaking.

b. Confidence

How confident are you that your scheduler works correctly?

What edge cases would you test next if you had more time?

I'm confident the scheduler handles the main use cases well, but if I had more time I would test more edge cases such as overlapping tasks across multiple pets or invalid inputs.

5. Reflection

a. What went well

What part of this project are you most satisfied with?

I'm very satisfied with how the scheduling logic came together, especially adding the smarter features like sorting tasks, recurring tasks, and conflict detection.

b. What you would improve

If you had another iteration, what would you improve or redesign?

I would improve the UI to show more task details like completion status and possibly add better conflict resolution instead of just warning messages.

c. Key takeaway

What is one important thing you learned about designing systems or working with AI on this project?

Using separate chat sessions for different phases like design, implementation, and testing helped keep the work organized. I learned that when working with AI tools like Copilot, it's important to guide the suggestions and make decisions about the design instead of blindly accepting everything.