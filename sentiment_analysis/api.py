from flask import Flask, abort, request, jsonify
from ml.sentiment_analysis import SentimentAnalysis as sa
import json

class Api():
    app = Flask(__name__)
    port = 101
    debug = False
    host = '0.0.0.0'

    @app.route('/', methods=['POST'])
    def compute():
        content = request.json

        if content['algo'] == 'sentiment':
            if content['process'] == 'predict':
                content = content['json']

                object = sa(content['text']).sentiment

                return jsonify (
                    polarity=object.polarity,
                    subjectivity=object.subjectivity,
                )

    def run(self):
        self.app.run (
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == '__main__':
    api = Api().run()
