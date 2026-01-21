from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def detect_emotion(text):
    score = sia.polarity_scores(text)['compound']

    if score >= 0.4:
        return "positive", score
    elif score <= -0.4:
        return "negative", abs(score)
    else:
        return "neutral", abs(score)
