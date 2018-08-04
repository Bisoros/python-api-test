import pickle
import numpy as np

class Ml():
    algo = []
    supervised_algos = ['LinearRegression', 'DecisionTreeClassifier']
    unsupervised_algos = ['PCA']
    name = ''

    def __init__(self, algo):
        self.algo = algo
        self.name = self.algo.__class__.__name__
        #if self.name

    def train(self, X, Y):
        # Input preprocessing
        X = np.asarray(X)
        X = np.reshape(X, (-1, 1))

        # Train the model using the training sets
        if :
            self.algo.fit(X, Y)


        #  Model persistence
        pickle.dump(self.algo, open('ml/model.pk', 'wb'))

    def predict(self, X):
        # Input preprocessing
        X = np.asarray(X)
        X = np.reshape(X, (-1, 1))

        # Load trained model from file
        self.algo = pickle.load(open('ml/model.pk', 'rb'))

        # Model inference
        Y = self.algo.predict(X)

        return list(Y)

    def test_linear_regression(self):
        # Test function to generate pickle file with dummy linear regression model

        X = [1, 2, 3, 4]
        Y = [2, 4, 6, 8]
        self.train(X, Y)

    def test_decision_tree(self):
        # Test function to generate pickle file with dummy decision tree model

        X = [1, 2, 3, 4]
        Y = [0, 0, 1, 1]
        self.train(X, Y)
