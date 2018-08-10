import ml.linear_regression as linear_regression
import ml.decision_tree as decision_tree
from rpc_server import RpcServer
import json

def compute(data):
    content = json.loads(data)

    if content['algo'] == 'regression':
        object = linear_regression.init()
        print ("hello there")
        if content['process'] == 'predict':
            content = content['json']
            X = content['input']
            print ("hello there 2")
            results=object.predict(X)

        elif content['process'] == 'train':
            content = content['json']
            X = content['input']
            Y = content['output']

            results=object.train(X, Y)

    elif content['algo'] == 'classification':
        object = decision_tree.init()

        if content['process'] == 'predict':
            content = content['json']
            X = content['input']

            results=object.predict(X)

        elif content['process'] == 'train':
            content = content['json']
            X = content['input']
            Y = content['output']

            results=object.train(X, Y)

    return json.dumps ({
        'results' : results,
    })


RpcServer('numbers', compute)
