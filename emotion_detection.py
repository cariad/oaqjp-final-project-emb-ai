import json
import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    body = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=body, headers=headers)  

    predictions = json.loads(response.text)
    emotions = predictions["emotionPredictions"][0]["emotion"]
    dominant = ""

    for emotion, score in emotions.items():
        if score > emotions.get(dominant, -1):
            dominant = emotion

    emotions["dominant_emotion"] = dominant

    return emotions

