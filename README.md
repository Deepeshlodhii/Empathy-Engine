# 🎙️ The Empathy Engine – Emotion-Aware Text-to-Speech System

The Empathy Engine is an AI-powered service that converts plain text into emotionally expressive speech.  
Unlike traditional monotonic TTS systems, this project detects the emotion in the input text and dynamically modulates vocal characteristics such as pitch, speaking rate, volume, and prosody to produce more human-like and emotionally resonant audio output.

This project demonstrates how sentiment analysis and modern neural TTS systems can be combined to build next-generation voice assistants for sales, customer support, and conversational AI.

---

## 🚀 Features

- Accepts text input via CLI or Web UI
- Emotion detection (Positive / Negative / Neutral)
- Emotion intensity scaling
- Dynamic voice modulation:
  - Pitch
  - Speaking rate
  - Volume / stability
  - Prosody & speaking style
- High-quality neural speech synthesis (ElevenLabs or Google TTS)
- Generates downloadable `.wav` audio output
- Flask-based web demo interface

---

## 🧠 System Architecture

```

Text Input
│
▼
Emotion Detection (VADER)
│
▼
Emotion + Intensity Mapping Logic
│
▼
TTS Engine (ElevenLabs / Google Cloud)
│
▼
Emotional Audio Output (.wav)

```

---

## 🛠️ Tech Stack

- Python 3.9+
- NLTK (VADER Sentiment Analyzer)
- Flask (Web UI)
- ElevenLabs API / Google Cloud Text-to-Speech
- Requests

---

## 📂 Project Structure

```

empathy-engine/
│
├── app.py                    # CLI application
├── web_app.py                # Flask web interface
├── emotion.py                # Emotion detection logic
├── tts_engine_elevenlabs.py  # Emotional TTS engine
├── requirements.txt
├── output/
│   └── speech.wav
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone (https://github.com/Deepeshlodhii/Empathy-Engine)
cd empathy-engine
````

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download NLTK Sentiment Model

Run once:

```bash
python
```

```python
import nltk
nltk.download('vader_lexicon')
exit()
```

---

### 5. Configure TTS API

#### Option A – ElevenLabs

1. Create account: [https://elevenlabs.io](https://elevenlabs.io)
2. Generate API key (enable "Text to Speech" permission)
3. Paste API key into:

```python
API_KEY = "your_api_key_here"
```

inside `tts_engine_elevenlabs.py`

(Optional: use `.env` for security)

---

#### Option B – Google Cloud TTS (alternative)

Follow Google Cloud TTS setup if ElevenLabs free tier is blocked.

---

## ▶️ Running the Application

---

### CLI Version

```bash
python app.py
```

Enter any text when prompted.

---

### Web Interface Version

```bash
python web_app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Example Inputs

**Positive**

> This is the best day of my life! Everything finally worked out!

**Negative**

> I am extremely disappointed and frustrated with this service.

**Neutral**

> The meeting is scheduled for tomorrow at 10 AM.

---

## 🎛️ Design Choices & Emotion-to-Voice Mapping

### 1. Emotion Detection

We use **VADER Sentiment Analysis (NLTK)** to compute a compound sentiment score:

| Score Range | Emotion  |
| ----------- | -------- |
| ≥ 0.4       | Positive |
| ≤ -0.4      | Negative |
| Otherwise   | Neutral  |

The absolute value of the compound score is used as **emotion intensity**.

---

### 2. Voice Parameter Mapping Logic

Each detected emotion maps to a specific vocal configuration:

| Emotion  | Pitch  | Rate   | Volume / Stability | Speaking Style |
| -------- | ------ | ------ | ------------------ | -------------- |
| Positive | High   | Fast   | High energy        | Expressive     |
| Negative | Low    | Slow   | Softer             | Calm / serious |
| Neutral  | Normal | Normal | Balanced           | Neutral        |

---

### 3. Intensity Scaling

Emotion intensity dynamically controls how strong the modulation is:

Example:

| Text                           | Effect                     |
| ------------------------------ | -------------------------- |
| "This is good."                | Slight pitch increase      |
| "This is the best day ever!!!" | Strong pitch + faster rate |

---

### 4. TTS Engine Choice

We selected **neural TTS (ElevenLabs / Google Cloud)** because:

* Supports pitch control
* Supports prosody
* Produces human-like voices
* Allows programmatic control
* Works with SSML

---

## 📌 Assignment Requirements Checklist

| Requirement                     | Status |
| ------------------------------- | ------ |
| Text Input                      | ✅      |
| Emotion Detection (≥ 3 classes) | ✅      |
| Rate modulation                 | ✅      |
| Pitch modulation                | ✅      |
| Volume modulation               | ✅      |
| Emotion-to-voice mapping        | ✅      |
| Audio output (.wav)             | ✅      |
| Web interface                   | ✅      |
| Intensity scaling               | ✅      |

---

## 🌱 Future Improvements

* Transformer-based emotion classifier (6+ emotions)
* SSML fine-grained emphasis control
* Multiple voice profiles
* Language detection
* Real-time streaming audio
* Cloud deployment (Render / Docker)

---

## 👨‍💻 Author

**Deepesh Lodhi**
AI & Data Science Enthusiast
IIT Delhi



