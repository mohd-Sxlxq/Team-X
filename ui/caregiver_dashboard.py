import streamlit as st
from backend.reminder_storage import save_reminder
from backend.user_storage import get_my_seniors
from backend.storage import get_last_7_records
import pandas as pd
import os
import matplotlib.pyplot as plt

def show_caregiver_dashboard():
    st.markdown("""
<style>
.main { background:#f4f8ff; }
.card {
    background:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.05);
}
.section-title {
    color:#2c7be5;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

    st.title("👨‍⚕️ Caregiver Dashboard")

    caregiver = st.session_state.username
    seniors = get_my_seniors(caregiver)

    # ================= SENIORS CARD =================
    st.markdown("### 👥 My Seniors")

    if seniors:
        cols = st.columns(len(seniors))
        for i, s in enumerate(seniors):
            with cols[i]:
                st.info(f"🧓 {s}")
    else:
        st.warning("No seniors assigned yet")

    st.markdown("---")

    # ================= PRESCRIBE CARD =================
    st.markdown("### 💊 Prescribe Medication")

    if seniors:

        with st.container():

            selected_senior = st.selectbox("Assign to Senior", seniors)

            col1, col2 = st.columns(2)

            with col1:
                med = st.text_input("Medicine Name")

            with col2:
                st.write(" ")

            col3, col4 = st.columns(2)

            with col3:
                start = st.time_input("Start Time")

            with col4:
                end = st.time_input("End Time")

            if st.button("➕ Add Reminder", use_container_width=True):
                save_reminder(med, str(start), str(end), selected_senior)
                st.success(f"Reminder added for {selected_senior}")

    st.markdown("---")

    # ================= MEDICATION ADHERENCE =================
    st.markdown("### 📊 Medication Adherence (%)")

    FILE_PATH = "data/reminders.xlsx"

    if os.path.exists(FILE_PATH):

        df = pd.read_excel(FILE_PATH)

        if not df.empty:

            total = df.groupby("Senior")["Taken"].count()
            taken = df[df["Taken"] == "Yes"].groupby("Senior")["Taken"].count()

            adherence = (taken / total) * 100
            adherence = adherence.fillna(0)

            st.bar_chart(adherence)

    st.markdown("---")

    # ================= HEALTH TRENDS =================
    st.markdown("### 📈 Health Trends")

    if seniors:

        selected = st.selectbox("Select Senior", seniors, key="health_select")

        data = get_last_7_records(selected)

        if data is not None:

            data["Label"] = data["Date"] + " " + data["Time"]

            col1, col2, col3 = st.columns(3)

            # ---------- BP ----------
            with col1:
                st.markdown("#### ❤️ Blood Pressure")
                fig1 = plt.figure()
                plt.plot(data["Label"], data["Blood Pressure"], marker='o')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig1)

            # ---------- Sugar ----------
            with col2:
                st.markdown("#### 🍬 Sugar Level")
                fig2 = plt.figure()
                plt.plot(data["Label"], data["Sugar Level"], marker='o')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig2)

            # ---------- HR ----------
            with col3:
                st.markdown("#### 💓 Heart Rate")
                fig3 = plt.figure()
                plt.plot(data["Label"], data["Heart Rate"], marker='o')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig3)

        else:
            st.info("No health data yet")