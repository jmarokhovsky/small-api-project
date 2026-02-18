from flask import Flask, jsonify
from flask_restful import Resources, Api, regparse
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = Flask(__name__)
api = Api(app)

output = {}


def sentiment(sentence):
    nltk.download("vader_lexicon")
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)["compound"]
    if score > 0:
        return "Positive"
    else:
        return "Negative"


@app.route("/", methods=["GET", "POST"])
def sentimentRequest():
    if request.method == "POST":
        sentence = request.form["q"]
    else:
        sentence = request.args.get("q")

    sent = sentiment(sentence)
    print(sentence)
    output["sentiment"] = sent
    return jsonify(output)


if __name__ == "__main__":
    app.run()
