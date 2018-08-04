from flask import Flask, abort, request, jsonify
from ml import ml
import json

class Api():
    app = Flask(__name__)
    port = 420
    debug = False
    host = '0.0.0.0'

    @app.route('/')
    def hello_world():
        return 'Hello world!'

    @app.route('/test/<var>')
    def test(var):
        return var

    @app.route('/<type>/<task>/<process>', methods=['POST'])
    def compute(type, task, process):
        if type == 'numbers':
            if task == 'regression':
                if process == 'predict':
                    content = request.json
                    X = content['input']
                    return jsonify (
                        results=ml.predict(X),
                    )
                elif process == 'train':
                    content = request.json
                    X = content['input']
                    Y = content['output']
                    return jsonify (
                        return = ml.train(X, Y),
                    )

        elif type == 'vision':
            return 'vision'

        elif type == 'sound':
            return 'sound'

        elif type == 'text':
            return 'text'

    def run(self):
        self.app.run (
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == '__main__':
    api = Api().run()
