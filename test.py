from flask import Flask, abort, request
import json

app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    print (request.get_json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
