import streamlit as st

def todo_list_page():
    # Initialize tasks list in session state if not already set
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    st.title("To-Do List")

    # Input field for new tasks
    new_task = st.text_input("Enter a new task:")

    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "completed": False})
            st.success("Task added!")
            # No need for st.experimental_rerun() here

    # Display the list of tasks with checkboxes for completion status
    if st.session_state.tasks:
        st.write("Tasks:")
        for idx, task in enumerate(st.session_state.tasks):
            col1, col2, col3 = st.columns([2, 6, 2])
            with col1:
                checkbox = st.checkbox("", value=task["completed"], key=f"checkbox_{idx}")
                if checkbox != task["completed"]:
                    st.session_state.tasks[idx]["completed"] = checkbox
                    st.success("Task updated!")
            with col2:
                st.write(task["task"])
            with col3:
                if st.button("Edit", key=f"edit_{idx}"):
                    new_task_value = st.text_input("Edit Task", value=task["task"], key=f"edit_input_{idx}")
                    if st.button("Save", key=f"save_{idx}"):
                        st.session_state.tasks[idx]["task"] = new_task_value
                        st.success("Task updated!")
                if st.button("Delete", key=f"delete_{idx}"):
                    st.session_state.tasks.pop(idx)
                    st.success("Task deleted!")

    else:
        st.write("No tasks yet.")

    # Option to clear all tasks
    if st.button("Clear All Tasks"):
        st.session_state.tasks.clear()
        st.success("All tasks cleared!")

    # Option to save tasks to a file
    if st.button("Save to File"):
        with open("tasks.txt", "w") as f:
            for task in st.session_state.tasks:
                status = "Completed" if task["completed"] else "Pending"
                f.write(f"{task['task']} - {status}\n")
        st.success("Tasks saved to file!")
