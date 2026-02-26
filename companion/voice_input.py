import speech_recognition as sr

def listen_to_senior():

    r = sr.Recognizer()

    mic_list = sr.Microphone.list_microphone_names()

    # Prefer Bluetooth if connected
    preferred_mic = None

    for i, name in enumerate(mic_list):
        if "Headset" in name or "Bluetooth" in name:
            preferred_mic = i
            break

    # Else fallback to Realtek laptop mic
    if preferred_mic is None:
        for i, name in enumerate(mic_list):
            if "Microphone" in name and "Realtek" in name:
                preferred_mic = i
                break

    # Else default mic
    if preferred_mic is None:
        preferred_mic = 0

    print(f"Using Mic: {mic_list[preferred_mic]}")

    with sr.Microphone(device_index=preferred_mic) as source:

        r.pause_threshold = 0.5   # faster detection
        r.energy_threshold = 300  # improves sensitivity

        print("Listening... Speak now")

        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            return "No speech detected."

    try:
        text = r.recognize_google(audio, language="en-IN")
        text = text.lower()

        # -------- Medical Correction Layer --------
        corrections = {
            "head egg": "headache",
            "head ache": "headache",
            "dick": "headache",
            "sugar level": "sugar",
            "shower": "sugar",
            "hurt rate": "heart rate",
            "hot rate": "heart rate",
            "heartbeat": "heart rate",
            "pain in my head": "headache"
        }

        for wrong, correct in corrections.items():
            if wrong in text:
                text = text.replace(wrong, correct)

        return text

    except:
        return "Sorry, I didn't understand."