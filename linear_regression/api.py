from flask import Flask, abort, request, jsonify
import ml.linear_regression as linear_regression
import ml.decision_tree as decision_tree
import json

class MLWrapperApi():
    app = Flask(__name__)
    port = 100
    debug = False
    host = '0.0.0.0'

    @app.route('/', methods=['POST'])
    def compute():
        content = request.json
        print(request.form)

        if content['algo'] == 'regression':
            object = linear_regression.init()

            if content['process'] == 'predict':
                content = content['json']
                X = content['input']
                return jsonify (
                    results=object.predict(X),
                )
            elif content['process'] == 'train':
                content = content['json']
                X = content['input']
                Y = content['output']
                return jsonify (
                    results=object.train(X, Y),
                )
        elif content['algo'] == 'classification':
            object = decision_tree.init()

            if content['process'] == 'predict':
                content = content['json']
                X = content['input']
                return jsonify (
                    results=object.predict(X),
                )
            elif content['process'] == 'train':
                content = content['json']
                X = content['input']
                Y = content['output']
                return jsonify (
                    results=object.train(X, Y),
                )

    def run(self):
        self.app.run (
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == '__main__':
    api = MLWrapperApi().run()
