import pandas as pd
import os
from datetime import datetime

FILE_PATH = "data/reminders.xlsx"

def save_reminder(med, start, end, senior):

    import pandas as pd
    import os

    FILE_PATH = "data/reminders.xlsx"

    new_data = {
        "Senior": [senior],
        "Medicine": [med],
        "Start": [start],
        "End": [end],
        "Taken": ["No"],
        "Notified": ["No"]   # 👈 NEW
    }

    new_df = pd.DataFrame(new_data)

    if os.path.exists(FILE_PATH):
        old_df = pd.read_excel(FILE_PATH)
        combined = pd.concat([old_df, new_df], ignore_index=True)
    else:
        combined = new_df

    combined.to_excel(FILE_PATH, index=False)


def get_reminders_for_senior(senior):

    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH)
        return df[df["Senior"] == senior]

    return pd.DataFrame()


def mark_taken(index):

    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH)
        df.loc[index, "Taken"] = "Yes"
        df.to_excel(FILE_PATH, index=False)

def mark_notified(index):

    import pandas as pd
    FILE_PATH = "data/reminders.xlsx"

    df = pd.read_excel(FILE_PATH)

    df.at[index, "Notified"] = "Yes"

    df.to_excel(FILE_PATH, index=False)