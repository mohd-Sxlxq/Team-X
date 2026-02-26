import pandas as pd
import os
from datetime import datetime

os.makedirs("data", exist_ok=True)

def get_file(senior):
    return f"data/health_{senior}.xlsx"


# ================= SAVE =================
def save_health_record(senior, bp, sugar, hr, risk):

    FILE_PATH = get_file(senior)

    now = datetime.now()

    new_data = {
        "Date": [now.strftime("%Y-%m-%d")],
        "Time": [now.strftime("%H:%M")],
        "Blood Pressure": [bp],
        "Sugar Level": [sugar],
        "Heart Rate": [hr],
        "Risk Level": [risk]
    }

    new_df = pd.DataFrame(new_data)

    if os.path.exists(FILE_PATH):
        old_df = pd.read_excel(FILE_PATH)
        combined = pd.concat([old_df, new_df], ignore_index=True)
    else:
        combined = new_df

    combined.to_excel(FILE_PATH, index=False)


# ================= LAST 7 =================
def get_last_7_records(senior):

    FILE_PATH = get_file(senior)

    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH)
        return df.tail(7)

    return None


# ================= LATEST HEALTH =================
def get_latest_health(senior):

    FILE_PATH = get_file(senior)

    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH)

        if not df.empty:
            last = df.iloc[-1]
            return last["Blood Pressure"], last["Sugar Level"], last["Heart Rate"]

    return None, None, None