from sklearn import linear_model
import pickle
import numpy as np

def train(X, Y):
    # Create linear regression object
    model = linear_model.LinearRegression()

    # Train the model using the training sets
    model.fit(X, Y)

    #  Model persistence
    s = pickle.dump(model, open( 'model.pk', 'wb' ))

def predict(X):
    X = np.asarray(X)
    X = np.reshape(X, (-1, 1))

    model = pickle.load(open( 'model.pk', 'rb' ))

    Y = model.predict(X)

    return Y

def test():
    X = [1, 2, 3, 4]
    Y = [2, 4, 6, 8]

    X = np.reshape(X, (-1, 1))
    train(X, Y)
