from sklearn import linear_model
import pickle
import numpy as np

def train(X, Y):
    # Input preprocessing
    X = np.asarray(X)
    X = np.reshape(X, (-1, 1))

    # Create linear regression object
    model = linear_model.LinearRegression()

    # Train the model using the training sets
    model.fit(X, Y)

    #  Model persistence
    pickle.dump(model, open( 'model.pk', 'wb' ))

def predict(X):
    # Input preprocessing
    X = np.asarray(X)
    X = np.reshape(X, (-1, 1))

    # Load trained model from file
    model = pickle.load(open( 'model.pk', 'rb' ))

    # Model inference
    Y = model.predict(X)

    return Y

def test():
    # Test function to generate pickle file with dummy regression model
    X = [1, 2, 3, 4]
    Y = [2, 4, 6, 8]

    train(X, Y)
