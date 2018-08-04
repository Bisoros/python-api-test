from sklearn import linear_model
import pickle
import numpy as np

class Ml(algo):
    def train(self, X, Y):
        # Input preprocessing
        X = np.asarray(X)
        X = np.reshape(X, (-1, 1))

        # Train the model using the training sets
        algo.fit(X, Y)

        #  Model persistence
        pickle.dump(algo, open( 'model.pk', 'wb' ))

    def predict(self, X):
        # Input preprocessing
        X = np.asarray(X)
        X = np.reshape(X, (-1, 1))

        # Load trained model from file
        algo = pickle.load(open( 'model.pk', 'rb' ))

        # Model inference
        Y = algo.predict(X)

        return Y

    def test(self):
        # Test function to generate pickle file with dummy regression model

        X = [1, 2, 3, 4]
        Y = [2, 4, 6, 8]
        train(X, Y)
