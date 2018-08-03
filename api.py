from flask import Flask, abort, request, jsonify
from ml import ml
import json

class Api():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello world!'

    @app.route('/predict', methods=['POST'])
    def predict():
        content = request.json
        X = content['input']
        return jsonify (
            results=ml.predict(X)
        )

    @app.route('/train', methods=['POST'])
    def train():
        content = request.json
        X = content['input']
        Y = content['output']
        return ml.train(X, Y)

    def run(self):
        self.app.run (
            host='0.0.0.0',
            port=420,
            debug=False,
        )

if __name__ == '__main__':
    api = Api().run()
