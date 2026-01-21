import requests
import os

API_KEY = "sk_0c9283c4eddc540f1b038d808de96-------aa60"

VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel (default high quality voice)

def generate_speech(text, emotion, intensity, filename="output/speech.wav"):

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    # Emotion → voice settings mapping
    emotion_settings = {
        "positive": {
            "stability": 0.25,
            "similarity_boost": 0.85
        },
        "negative": {
            "stability": 0.75,
            "similarity_boost": 0.45
        },
        "neutral": {
            "stability": 0.5,
            "similarity_boost": 0.6
        }
    }

    settings = emotion_settings.get(emotion, emotion_settings["neutral"])

    payload = {
        "text": text,
        "voice_settings": settings
    }

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception("ElevenLabs API Error:", response.text)

    os.makedirs("output", exist_ok=True)

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename

