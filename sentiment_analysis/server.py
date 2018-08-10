from ml.sentiment_analysis import SentimentAnalysis
from rpc_server import RpcServer
import json

def compute(data):
    content = json.loads(data)

    if content['algo'] == 'sentiment':
        if content['process'] == 'predict':
            content = content['json']
            text = content['text']
            object = SentimentAnalysis(text).sentiment

            return json.dumps ({
                'polarity' : object.polarity,
                'subjectivity' : object.subjectivity,
            })

RpcServer('text', compute)
