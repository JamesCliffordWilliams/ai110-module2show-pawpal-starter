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

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

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
