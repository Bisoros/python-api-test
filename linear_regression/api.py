from flask import Flask, abort, request, jsonify
import ml.linear_regression as lg
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

        object = lg.init()
        if content['algo'] == 'regression':
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
