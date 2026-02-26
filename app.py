import streamlit as st
from ui.auth import show_auth
from ui.senior_dashboard import show_senior_dashboard
from ui.caregiver_dashboard import show_caregiver_dashboard


st.set_page_config(
    page_title="Arogya Setu Senior+",
    page_icon="💙"
    
)

st.markdown("""
<style>
.main { background:#f4f8ff; }
.sidebar .sidebar-content {
    background:white;
}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if not st.session_state.logged_in:
    show_auth()

else:
    with st.sidebar:
        st.markdown("## 💙 Arogya Setu")
        st.markdown("---")
        st.markdown(f"👤 **{st.session_state.username.capitalize()}**")
        st.markdown(f"🔐 {st.session_state.role}")
        st.markdown("---")

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.role = None
            st.rerun()

    if st.session_state.role == "Senior":
        show_senior_dashboard()

    elif st.session_state.role == "Caregiver":
        show_caregiver_dashboard()