from flask import Flask, abort, request
from ml import ml
import json

class Api():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello world!'

    @app.route('/predict', methods=['POST'])
    def predict():
        content = request.form
        X = int(content.get('input'))
        return str(ml.predict(X)[0])


    def run(self):
        self.app.run(host='0.0.0.0', port=420, debug=False)

if __name__ == '__main__':
    api = Api().run()
