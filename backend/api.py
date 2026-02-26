from fastapi import FastAPI
from backend.storage import save_health_record
from backend.email_alert import send_email_alert

app = FastAPI()

def calculate_risk(bp, sugar, hr):

    if bp > 160 or sugar > 250 or hr > 120:
        return "High Risk"

    elif bp > 140 or sugar > 180 or hr > 100:
        return "Warning"

    else:
        return "Normal"

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/submit-health")
def submit_health(senior: str, bp: float, sugar: float, hr: float):

    risk = calculate_risk(bp, sugar, hr)

    save_health_record(senior, bp, sugar, hr, risk)

    if risk == "High Risk":
        send_email_alert(senior, bp, sugar, hr, risk)

    return {"risk_level": risk}