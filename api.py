from flask import Flask
from ml import ml

class Api():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return str(ml.predict(2))

    def run(self):
        self.app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    api = Api().run()
