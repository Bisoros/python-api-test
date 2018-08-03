from flask import Flask, abort, request, jsonify
from ml import ml
import json

class Api():
    app = Flask(__name__)

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
                        results=ml.predict(X)
                    )
                elif process == 'train':
                    content = request.json
                    X = content['input']
                    Y = content['output']
                    return ml.train(X, Y)

        elif type == 'vision':
            return 'vision'

        elif type == 'sound':
            return 'sound'

        elif type == 'text':
            return 'text'

    def run(self):
        self.app.run (
            host='0.0.0.0',
            port=420,
            debug=False,
        )

if __name__ == '__main__':
    api = Api().run()
