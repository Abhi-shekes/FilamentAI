# components/signup.py
import streamlit as st
from utils.db import get_user_collection
import hashlib

def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        if username and password:
            users = get_user_collection()
            if users.find_one({"username": username}):
                st.error("Username already exists!")
            else:
                # Simple SHA256 hash; consider using a more secure hashing mechanism in production
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                users.insert_one({"username": username, "password": hashed_password})
                st.success("Account created successfully!")
        else:
            st.error("Please provide both username and password.")
