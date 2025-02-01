# components/login.py
import streamlit as st
from utils.db import get_user_collection
import hashlib

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username and password:
            users = get_user_collection()
            user = users.find_one({"username": username})
            if user:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if user["password"] == hashed_password:
                    st.success("Logged in successfully!")
                    # Optionally, save user info in session_state for later use
                    st.session_state["username"] = username
                else:
                    st.error("Invalid password!")
            else:
                st.error("Username not found!")
        else:
            st.error("Please provide both username and password.")
