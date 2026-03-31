from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = Flask(__name__)
api = Api(app)

output = {}

# Argument parsing
parser = reqparse.RequestParser()
parser.add_argument("q", help="Pass a sentence to analyze")


class SentimentAnalysis(Resource):

    def get(self):
        # Use parser to find the user's query
        args = parser.parse_args()
        sentence = args["q"]

        # Analyze the sentence that came from the args
        nltk.download("vader_lexicon")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(sentence)["compound"]
        if score > 0:
            output["sentiment"] = "positive"
        else:
            output["sentiment"] = "negative"

        return jsonify(output)


# use for flask_restful
api.add_resource(SentimentAnalysis, "/")

if __name__ == "__main__":
    app.run()
