from flask import Flask, abort, request, jsonify
from rpc_client import RpcClient
import json, requests

class Api():
    app = Flask(__name__)
    port = 420
    debug = True
    host = '0.0.0.0'
    global ports, create_json

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
        global create_json

        data = create_json(task, process, request.json)
        print (json.dumps(data))

        # create queue, send and receive response
        # TODO: validate type
        rpc = RpcClient(type)
        response = rpc.call(json.dumps(data))

        return response

    # start server
    def run(self):
        self.app.run (
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == '__main__':
    api = Api().run()
