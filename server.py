from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)
    return response

@app.route("/")
def home():
    return "Emotion Detector Application Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)