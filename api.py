from flask import Flask, abort, request, jsonify
import json, requests

class Api():
    app = Flask(__name__)
    port = 420
    debug = False
    host = '0.0.0.0'
    global ports, create_json
    ports = {
        'numbers' : '100',
        'text' : '101',
    }

    def create_json(task, process, req_json):
        return {
            'algo' : task,
            'process' : process,
            'json' : req_json,
        }

    @app.route('/')
    def hello_world():
        return 'Hello world!'

    @app.route('/test/<var>')
    def test(var):
        return var

    @app.route('/<type>/<task>/<process>', methods=['POST'])
    def compute(type, task, process):
        global property, create_json

        postdata = create_json(task, process, request.json)
        url = 'http://0.0.0.0:' + ports[type]
        r = requests.post(url, json=postdata)
        return r.text

    def run(self):
        self.app.run (
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == '__main__':
    api = Api().run()
