from openai import OpenAI
from backend.storage import get_latest_health
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def companion_reply(message, history=[]):

    senior = os.getenv("CURRENT_SENIOR", "default")

    bp, sugar, hr = get_latest_health(senior)

    system_prompt = f"""
You are a caring AI companion for elderly users.

Latest health data of the user:
Blood Pressure: {bp}
Sugar Level: {sugar}
Heart Rate: {hr}

If the user asks about health:
Use these values to answer.

Health meaning:

BP:
>160 → High
140–160 → Slightly High
<140 → Normal

Sugar:
>250 → High
180–250 → Slightly High
<180 → Normal

Heart Rate:
>120 → High
100–120 → Slightly High
<100 → Normal

Speak simply and supportively.
"""

    messages = [{"role": "system", "content": system_prompt}]

    for h in history[-5:]:
        messages.append({"role": "user", "content": h})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content