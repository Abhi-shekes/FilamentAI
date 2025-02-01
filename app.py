# app.py
import streamlit as st
from components.login import login
from components.signup import signup

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Sign Up"])
    
    if page == "Login":
        login()
    elif page == "Sign Up":
        signup()

if __name__ == '__main__':
    main()
