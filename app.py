import streamlit as st
from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This demo shows how you can wire the UI into the backend logic.
Use the sections below to add pets, assign tasks, and generate a simple schedule.
"""
)

# --- Persist owner across reruns --------------------------------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner()

owner: Owner = st.session_state.owner

# --- Add a new pet --------------------------------------------------------------
with st.form("add_pet_form"):
    st.subheader("Add a pet")
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    breed = st.text_input("Breed", value="Mixed")
    dob = st.date_input("Date of birth", value=date(2020, 1, 1))

    if st.form_submit_button("Add pet"):
        pet = Pet(pet_name=pet_name, species=species, dob=dob, breed=breed)
        owner.add_pet(pet)
        st.success(f"Added pet: {pet_name}")

# --- Add tasks for a selected pet ------------------------------------------------
st.divider()
st.subheader("Add tasks")

if owner.pets:
    pet_names = [p.pet_name for p in owner.pets]
    selected_pet_name = st.selectbox("Select pet", pet_names)
    selected_pet = next(p for p in owner.pets if p.pet_name == selected_pet_name)

    with st.form("add_task_form"):
        task_name = st.text_input("Task name", value="Feed")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        priority = st.selectbox("Priority", [1, 2, 3, 4, 5], index=2)

        if st.form_submit_button("Add task"):
            task = Task(task_name=task_name, duration=int(duration), priority=int(priority))
            selected_pet.add_task(task)
            st.success(f"Added task '{task_name}' to {selected_pet.pet_name}")
else:
    st.info("Add a pet first to start assigning tasks.")

# --- Show pets and tasks --------------------------------------------------------
st.divider()
st.subheader("Pets & Tasks")

if owner.pets:
    for pet in owner.pets:
        st.markdown(f"**{pet.pet_name}** ({pet.species}, {pet.breed})")
        if pet.tasks:
            for t in pet.tasks:
                st.write(f"- {t.task_name} (duration: {t.duration}m, priority: {t.priority})")
        else:
            st.write("- No tasks assigned yet.")
else:
    st.info("No pets added yet.")

# --- Schedule generation --------------------------------------------------------
st.divider()
st.subheader("Generate schedule")

if st.button("Generate schedule"):
    if not owner.pets or not any(p.tasks for p in owner.pets):
        st.warning("Add at least one pet with a task before generating a schedule.")
    else:
        plan, warning = Scheduler.generate_daily_plan(owner, start_time="08:00")
        if warning:
            st.warning(f"⚠️ Scheduling Conflict: {warning}")
        schedule = plan.get_daily_schedule()
        scheduled_times = schedule.get("scheduled_times", {})

        # Sort tasks by time for display
        sorted_tasks = Scheduler.sort_by_time(plan.tasks, scheduled_times)

        st.markdown("### Today's Schedule")
        if sorted_tasks:
            # Display as a clean table
            table_data = [
                {"Time": scheduled_times.get(t.task_name, "N/A"), "Task": t.task_name, "Duration": f"{t.duration}m", "Priority": t.priority}
                for t in sorted_tasks
            ]
            st.table(table_data)
        else:
            st.info("No tasks to schedule.")
