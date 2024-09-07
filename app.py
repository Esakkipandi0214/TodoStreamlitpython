import streamlit as st
from todo import todo_list_page  # Import your To-Do list page function

# Mock function for login (replace with your actual login logic)
def login(username, password):
    # Simple login logic for testing purposes
    if username == "user" and password == "pass":  # Example credentials
        return True
    else:
        return False

# Initialize the session state for login status if not already set
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Function to display the login page
def show_login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True  # Set login status to True
            # Optionally clear any other session state data
            st.session_state.username = username
            st.success("Login successful!")
            # We don't need st.experimental_rerun() here
        else:
            st.error("Invalid username or password")

# Main app logic
if st.session_state.logged_in:
    # If logged in, show the To-Do List dashboard
    st.title("To-Do List Dashboard")
    todo_list_page()  # This function will render your To-Do list page

    # Option to log out
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        # We don't need st.experimental_rerun() here either
else:
    # If not logged in, show the login page
    show_login_page()
