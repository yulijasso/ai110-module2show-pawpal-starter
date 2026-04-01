import streamlit as st
from pawpal_system import Owner, Pet, Task, Priority, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", available_time=120)

owner = st.session_state.owner

st.title("🐾 PawPal+")

# ── Owner Setup ──────────────────────────────────────────────
st.subheader("Owner")
owner_name = st.text_input("Owner name", value=owner.name)
available_time = st.number_input(
    "Available time (minutes per day)", min_value=1, max_value=480, value=owner.available_time
)
owner.name = owner_name
owner.available_time = available_time

# ── Add a Pet ────────────────────────────────────────────────
st.divider()
st.subheader("Add a Pet")

col_p1, col_p2 = st.columns(2)
with col_p1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col_p2:
    species = st.selectbox("Species", ["dog", "cat", "other"])

pet_breed = st.text_input("Breed (optional)", value="")
pet_age = st.number_input("Age (years)", min_value=0, max_value=30, value=1)

if st.button("Add pet"):
    new_pet = Pet(name=pet_name, species=species, breed=pet_breed, age=pet_age)
    owner.add_pet(new_pet)
    st.success(f"Added {pet_name} the {species}!")

if owner.pets:
    st.write("Current pets:")
    st.table([{"Name": p.name, "Species": p.species, "Breed": p.breed, "Age": p.age} for p in owner.pets])
else:
    st.info("No pets yet. Add one above.")

# ── Add a Task to a Pet ──────────────────────────────────────
st.divider()
st.subheader("Add a Task")

if owner.pets:
    pet_choice = st.selectbox("Assign to pet", [p.name for p in owner.pets])

    col1, col2 = st.columns(2)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        recurrence = st.selectbox("Recurrence", ["None", "daily", "weekly"], index=0)
    with col2:
        category = st.selectbox("Category", ["walk", "feeding", "meds", "grooming", "enrichment"])
        priority = st.selectbox("Priority", ["HIGH", "MEDIUM", "LOW"], index=0)
        use_scheduled_time = st.checkbox("Set a scheduled time")

    scheduled_time = None
    if use_scheduled_time:
        sched_hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=8)
        sched_min = st.number_input("Minute (0-59)", min_value=0, max_value=59, value=0)
        scheduled_time = int(sched_hour) * 60 + int(sched_min)

    if st.button("Add task"):
        selected_pet = next(p for p in owner.pets if p.name == pet_choice)
        new_task = Task(
            name=task_title,
            duration=int(duration),
            priority=Priority[priority],
            category=category,
            recurrence=None if recurrence == "None" else recurrence,
            scheduled_time=scheduled_time,
        )
        selected_pet.add_task(new_task)
        st.success(f"Added '{task_title}' for {pet_choice}!")

    # ── Filter Tasks ─────────────────────────────────────────
    all_tasks = owner.get_all_tasks()
    if all_tasks:
        st.markdown("### Task List")
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            filter_pet = st.selectbox("Filter by pet", ["All"] + [p.name for p in owner.pets], key="filter_pet")
        with filter_col2:
            filter_status = st.selectbox("Filter by status", ["All", "Incomplete", "Completed"], key="filter_status")

        display_tasks = all_tasks
        if filter_pet != "All":
            display_tasks = [t for t in display_tasks if t.pet_name == filter_pet]
        if filter_status == "Incomplete":
            display_tasks = [t for t in display_tasks if not t.completed]
        elif filter_status == "Completed":
            display_tasks = [t for t in display_tasks if t.completed]

        if display_tasks:
            def fmt_time(t):
                if t.scheduled_time is not None:
                    h, m = divmod(t.scheduled_time, 60)
                    return f"{h:02d}:{m:02d}"
                return "-"

            st.table([
                {"Pet": t.pet_name, "Task": t.name, "Duration": t.duration,
                 "Priority": t.priority.name, "Category": t.category,
                 "Time": fmt_time(t), "Recurrence": t.recurrence or "-",
                 "Done": t.completed}
                for t in display_tasks
            ])
        else:
            st.info("No tasks match the current filters.")
else:
    st.info("Add a pet first, then you can assign tasks.")

# ── Generate Schedule ────────────────────────────────────────
st.divider()
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    if not owner.get_all_tasks():
        st.warning("Add at least one task before generating a schedule.")
    else:
        scheduler = Scheduler(owner)
        explanation = scheduler.get_explanation()
        st.code(explanation, language="text")
        if scheduler.conflicts:
            st.error(f"{len(scheduler.conflicts)} time conflict(s) detected — see details above.")
