import streamlit as st
import time
st.markdown("""
<style>
    .stApp {
        background-color: #4472C4;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Initialize task input field
if 'new_task_input' not in st.session_state:
    st.session_state.new_task_input = ""


def main():
    st.title("🎯 Task Management App")
    st.write("Welcome to your personal task manager!")

    # Sidebar for operations
    st.sidebar.header("Choose an Operation")
    operation = st.sidebar.selectbox(
        "What would you like to do?",
        ["Add Task", "View Tasks", "Update Task", "Delete Task"]
    )

    # Clear all tasks button - moved below choose operation
    if st.sidebar.button("🗑️ Clear All Tasks"):
        st.session_state.tasks = []
        st.sidebar.success("All tasks cleared!")
        st.rerun()

    # Display task count in sidebar
    st.sidebar.markdown("---")
    st.sidebar.write(f"**Total Tasks: {len(st.session_state.tasks)}**")

    # Main content area
    if operation == "Add Task":
        add_task()
    elif operation == "View Tasks":
        view_tasks()
    elif operation == "Update Task":
        update_task()
    elif operation == "Delete Task":
        delete_task()

def add_task():
    st.header("➕ Add New Task")
    new_task = st.text_input("Enter a new task: ")
    if st.button("Add Task"):
        if not new_task:
            st.warning("Please enter a task!")
        elif new_task in st.session_state.tasks:
            st.warning("Task already exists!")
        else:
            st.session_state.tasks.append(new_task)
            st.session_state.success_flag = f"Task '{new_task}' added successfully!"
            st.session_state.task_input = " "
            st.rerun()
    if 'success_flag' in st.session_state:
        st.success(st.session_state.success_flag)
        del st.session_state.success_flag

def view_tasks():
    st.header("📋 Your Tasks")

    if st.session_state.tasks:
        st.write("### Current Tasks:")
        for i, task in enumerate(st.session_state.tasks, 1):
            st.write(f"{i}. {task}")
    else:
        st.info("No tasks added yet! Use the sidebar to add some tasks.")

def update_task():
    st.header("✏️ Update Task")

    if not st.session_state.tasks:
        st.warning("No tasks available to update!")
        return

    # Show current tasks
    st.write("### Current Tasks:")
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {task}")

    # Select task to update
    task_to_update = st.selectbox("Select task to update:", st.session_state.tasks)
    new_task_value = st.text_input("Enter new task value:")

    if st.button("Update Task"):
        if new_task_value:
            index = st.session_state.tasks.index(task_to_update)
            old_task = st.session_state.tasks[index]
            st.session_state.tasks[index] = new_task_value

            st.session_state.task_input = ""

            st.session_state.success_flag = f"Task '{old_task}' updated to '{new_task_value}'!"
            st.rerun()
        else:
            st.warning("Please enter a new task value!")

    if 'success_flag' in st.session_state:
        st.success(st.session_state.success_flag)
        del st.session_state.success_flag


def delete_task():
    st.header("🗑️ Delete Task")

    if not st.session_state.tasks:
        st.warning("No tasks available to delete!")
        return

    # Show current tasks
    st.write("Current Tasks:")
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {task}")

    # Select task to delete
    task_to_delete = st.selectbox("Select task to delete:", st.session_state.tasks)

    if st.button("Delete Task", type="primary"):
        st.session_state.tasks.remove(task_to_delete)
        st.success(f"Task '{task_to_delete}' deleted successfully!")
        st.rerun()

if __name__ == "__main__":
    main()