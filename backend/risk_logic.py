def calculate_risk(bp, sugar, hr):

    if bp > 160 or sugar > 150 or hr > 120:
        return "High Risk, Message Sent to Caretaker"

    elif bp > 140 or sugar > 180 or hr > 100:
        return "Warning"

    else:
        return "Normal"