import pandas as pd
import os

FILE_PATH = "data/users.xlsx"
os.makedirs("data", exist_ok=True)

# -------- CREATE USER --------
def create_user(username, password, role, caregiver=""):

    username = str(username).strip().lower()
    password = str(password).strip()
    caregiver = str(caregiver).strip().lower()

    new_user = pd.DataFrame({
        "Username": [username],
        "Password": [password],
        "Role": [role],
        "Caregiver": [caregiver]
    })

    if os.path.exists(FILE_PATH):
        df = pd.read_excel(FILE_PATH, dtype=str).fillna("")

        df["Username"] = df["Username"].str.strip().str.lower()

        if username in df["Username"].values:
            return False

        df = pd.concat([df, new_user], ignore_index=True)
    else:
        df = new_user

    df.to_excel(FILE_PATH, index=False)
    return True


# -------- LOGIN --------
def authenticate_user(username, password):

    username = str(username).strip().lower()
    password = str(password).strip()

    if not os.path.exists(FILE_PATH):
        return None

    df = pd.read_excel(FILE_PATH, dtype=str).fillna("")

    df["Username"] = df["Username"].str.strip().str.lower()
    df["Password"] = df["Password"].str.strip()

    match = df[
        (df["Username"] == username) &
        (df["Password"] == password)
    ]

    if not match.empty:
        return match.iloc[0]["Role"]

    return None


# -------- GET ALL CAREGIVERS --------
def get_all_caregivers():

    if not os.path.exists(FILE_PATH):
        return []

    df = pd.read_excel(FILE_PATH, dtype=str).fillna("")

    caregivers = df[df["Role"] == "Caregiver"]

    return caregivers["Username"].str.lower().tolist()


# -------- GET MY SENIORS --------
def get_my_seniors(caregiver):

    caregiver = caregiver.strip().lower()

    if not os.path.exists(FILE_PATH):
        return []

    df = pd.read_excel(FILE_PATH, dtype=str).fillna("")

    seniors = df[
        (df["Role"] == "Senior") &
        (df["Caregiver"].str.lower() == caregiver)
    ]

    return seniors["Username"].tolist()