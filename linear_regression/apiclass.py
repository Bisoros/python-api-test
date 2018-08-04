from flask import Flask, abort, request, jsonify
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

    def run(self):
        self.app.run (
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == '__main__':
    api = Api().run()
