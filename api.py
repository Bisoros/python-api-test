from flask import Flask, abort, request, jsonify
import json, requests

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
            postdata = {
                'algo' : task,
                'process' : process,
                'json' : request.json,
            }

            url = 'http://0.0.0.0:100/'

            r = requests.post(url, json=postdata)
            print (r)
            print (r.text)
            return r.text

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
