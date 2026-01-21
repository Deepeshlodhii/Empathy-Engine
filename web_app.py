from flask import Flask, render_template_string, request, send_file
from emotion import detect_emotion
from tts_engine_elevenlabs import generate_speech   # 👈 changed here

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>The Empathy Engine</title>
</head>
<body>
    <h2>🎙️ The Empathy Engine (Emotional Voice)</h2>

    <form method="post">
        <textarea name="text" rows="5" cols="60" placeholder="Enter your text here..." required></textarea>
        <br><br>
        <button type="submit">Generate Emotional Voice</button>
    </form>

    {% if emotion %}
        <p><b>Detected Emotion:</b> {{ emotion }}</p>

        <audio controls>
            <source src="/audio" type="audio/wav">
            Your browser does not support audio playback.
        </audio>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = None

    if request.method == "POST":
        text = request.form["text"]

        emotion, intensity = detect_emotion(text)
        generate_speech(text, emotion, intensity)

    return render_template_string(HTML, emotion=emotion)


@app.route("/audio")
def audio():
    return send_file("output/speech.wav", mimetype="audio/wav")


if __name__ == "__main__":
    app.run(debug=True)
