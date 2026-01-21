import pyttsx3
import os

def generate_speech(text, emotion, intensity, filename="output/speech.wav"):
    engine = pyttsx3.init()

    # Default parameters
    rate = 170
    volume = 1.0

    # Emotion mapping
    if emotion == "positive":
        rate = int(170 + 40 * intensity)
        volume = 1.0
    elif emotion == "negative":
        rate = int(150 - 30 * intensity)
        volume = 0.8
    elif emotion == "neutral":
        rate = 165
        volume = 0.9

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    os.makedirs("output", exist_ok=True)

    engine.save_to_file(text, filename)
    engine.runAndWait()

    return filename
