import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to IBM Watson NLP emotion detection API
    and returns a formatted dictionary containing emotion scores
    and the dominant emotion.
    """

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {"error": "Invalid input. Text cannot be empty."}

    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze?version=2021-08-01"

    headers = {
        "Content-Type": "application/json"
    }

    json_data = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(
        url,
        json=json_data,
        headers=headers,
        auth=("apikey", "YOUR_API_KEY")
    )

    if response.status_code != 200:
        return {"error": "Failed to fetch emotion data."}

    response_json = response.json()

    emotions = response_json["emotion"]["document"]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions