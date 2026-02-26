from companion.voice_input import listen_to_senior
from companion.chatbot import companion_reply
from companion.voice_output import speak
import streamlit as st

def start_voice_chat(history):

    user_text = listen_to_senior()

    if user_text:

        # 🔹 Tell chatbot which senior is speaking
        import os
        os.environ["CURRENT_SENIOR"] = st.session_state.username

        ai_reply = companion_reply(user_text, history)

        speak(ai_reply)

        return user_text, ai_reply

    return "", ""