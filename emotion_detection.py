
import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores and the dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        url,
        json=input_data,
        headers=headers,
        timeout=30
    )

    if response.status_code == 200:
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(scores, key=scores.get)
        scores["dominant_emotion"] = dominant_emotion

        return scores

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }
