"""
Emotion analysis web app.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders and returns the index page.
    """

    return render_template('index.html')

@app.route("/emotionDetector")
def detector():
    """
    Analyses the emotion of text provided by the "textToAnalyze" argument
    and returns a descriptive explanation as an HTML fragment.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "<p><strong>Invalid text! Please try again!</strong></p>"

    # Get the name and score of every emotion, ignoring the dominant for now:
    emotions = [
        f"'{emotion}': {result[emotion]}" 
        for emotion in filter(lambda e: e != "dominant_emotion", result)
    ]

    # Create a comma-separated string with "and" between the final two:
    emotions_str = ", ".join(emotions[0:-1]) + " and " + emotions[-1]

    return (
        f"<p>For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>.</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
