from emotion import detect_emotion
from tts_engine_elevenlabs import generate_speech

def main():
    print("=== The Empathy Engine (Emotional Voice Edition) ===")
    text = input("Enter your text: ")

    emotion, intensity = detect_emotion(text)

    print(f"Detected Emotion: {emotion}")
    print(f"Emotion Intensity: {round(intensity, 2)}")

    output_file = generate_speech(text, emotion, intensity)

    print(f"Audio generated: {output_file}")

if __name__ == "__main__":
    main()
