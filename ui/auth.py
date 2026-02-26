import streamlit as st
from backend.user_storage import create_user, authenticate_user, get_all_caregivers

def show_auth():

    # ---------- CLEAN THEME ----------
    st.markdown("""
    <style>

    .main {
        background-color: #f4f8ff;
    }

    /* Card */
    .block-container {
        max-width: 500px;
        padding-top: 50px;
        margin: auto;
    }

    /* Remove Radio pill */
    div[role="radiogroup"] {
        display: flex;
        justify-content: center;
        gap: 20px;
        background: none !important;
    }

    div[role="radiogroup"] label {
        background: none !important;
        box-shadow: none !important;
        padding: 5px 15px;
        border-radius: 8px;
    }

    /* Inputs */
    .stTextInput > div > div,
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 10px;
        border: 1px solid #dbeafe;
    }

    /* Button */
    .stButton > button {
        background-color: #4c8bf5;
        color: white;
        border-radius: 10px;
        height: 45px;
        border: none;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

    st.title("🔐 Arogya Setu Senior+")

    menu = st.radio("", ["Login", "Signup"], horizontal=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    role = st.selectbox("Role", ["Senior", "Caregiver"])

    caregiver = ""

    if role == "Senior":
        caregivers = get_all_caregivers()
        if caregivers:
            caregiver = st.selectbox("Select Your Caregiver", caregivers)
        else:
            st.warning("No caregivers registered yet")

    # -------- SIGNUP --------
    if menu == "Signup":

        if st.button("Create Account", use_container_width=True):

            success = create_user(username, password, role, caregiver)

            if success:
                st.success("Account created! Please login.")
            else:
                st.error("Username already exists")

    # -------- LOGIN --------
    else:

        if st.button("Login", use_container_width=True):

            user_role = authenticate_user(username, password)

            if user_role:
                st.session_state.logged_in = True
                st.session_state.role = user_role
                st.session_state.username = username.lower()
                st.success("Login Successful")
                st.rerun()
            else:
                st.error("Invalid credentials")