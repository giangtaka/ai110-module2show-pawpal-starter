import streamlit as st
from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")

st.markdown(
    """
PawPal+ helps pet owners manage pets and schedule care tasks.
"""
)


# -----------------------------------
# SESSION STATE
# -----------------------------------

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

owner = st.session_state.owner
scheduler = Scheduler(owner)


# -----------------------------------
# ADD PET
# -----------------------------------

st.subheader("Add Pet")

pet_name = st.text_input(
    "Pet name",
    value="Mochi",
    key="add_pet_name"
)

species = st.selectbox(
    "Species",
    ["Dog", "Cat", "Other"],
    key="add_pet_species"
)

if st.button(
    "Add pet",
    key="add_pet_button"
):
    existing_names = [
        pet.name
        for pet in owner.pets
    ]

    if not pet_name.strip():
        st.warning("Please enter a pet name.")

    elif pet_name.strip() in existing_names:
        st.warning("That pet already exists.")

    else:
        new_pet = Pet(
            pet_name.strip(),
            species
        )

        owner.add_pet(new_pet)

        st.success(
            f"Added {pet_name.strip()}."
        )


# -----------------------------------
# SHOW PETS
# -----------------------------------

if owner.pets:
    st.subheader("Your Pets")

    for pet in owner.pets:
        st.write(
            f"🐾 {pet.name} ({pet.species})"
        )


# -----------------------------------
# ADD TASK
# -----------------------------------

if owner.pets:

    st.divider()

    st.subheader("Schedule Task")

    selected_pet_name = st.selectbox(
        "Choose pet",
        [pet.name for pet in owner.pets],
        key="task_pet"
    )

    task_description = st.text_input(
        "Task description",
        value="Morning walk",
        key="task_description"
    )

    task_time = st.time_input(
        "Time",
        key="task_time"
    )

    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=20,
        key="task_duration"
    )

    priority = st.selectbox(
        "Priority",
        ["low", "medium", "high"],
        index=2,
        key="task_priority"
    )

    frequency = st.selectbox(
        "Frequency",
        ["once", "daily", "weekly"],
        key="task_frequency"
    )

    if st.button(
        "Add task",
        key="add_task_button"
    ):

        if not task_description.strip():
            st.warning(
                "Please enter a task description."
            )

        else:
            selected_pet = next(
                pet
                for pet in owner.pets
                if pet.name == selected_pet_name
            )

            new_task = Task(
                description=task_description.strip(),
                time=task_time.strftime("%H:%M"),
                duration_minutes=int(duration),
                priority=priority,
                frequency=frequency,
                due_date=date.today()
            )

            selected_pet.add_task(new_task)

            st.success(
                f"Added '{task_description}' "
                f"for {selected_pet_name}."
            )


# -----------------------------------
# VIEW SCHEDULE
# -----------------------------------

st.divider()

st.subheader("Today's Schedule")

if st.button(
    "Generate schedule",
    key="generate_schedule_button"
):

    scheduled_tasks = scheduler.sort_by_time()

    if not scheduled_tasks:
        st.info(
            "No tasks scheduled yet."
        )

    else:
        for pet, task in scheduled_tasks:

            status = (
                "✅ Complete"
                if task.completed
                else "⏳ Pending"
            )

            st.write(
                f"**{task.time}** — "
                f"{pet.name}: "
                f"{task.description}"
            )

            st.caption(
                f"{task.duration_minutes} min | "
                f"Priority: {task.priority} | "
                f"Frequency: {task.frequency} | "
                f"{status}"
            )


# -----------------------------------
# CONFLICT DETECTION
# -----------------------------------

conflicts = scheduler.find_conflicts()

if conflicts:

    st.divider()

    st.subheader("⚠️ Schedule Conflicts")

    for conflict in conflicts:

        (pet1, task1), (pet2, task2) = conflict

        st.warning(
            f"{pet1.name}'s '{task1.description}' "
            f"conflicts with "
            f"{pet2.name}'s '{task2.description}' "
            f"at {task1.time}."
        )