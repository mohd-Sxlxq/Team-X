import pyttsx3
import threading

def speak(text):
    thread = threading.Thread(target=_speak, args=(text,), daemon=True)
    thread.start()

def _speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 140)
        engine.setProperty('volume', 0.9)

        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except:
        pass

def stop_speaking():
    try:
        engine = pyttsx3.init()
        engine.stop()
    except:
        pass