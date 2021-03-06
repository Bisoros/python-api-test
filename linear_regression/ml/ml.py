import pickle
import numpy as np

class Ml():
    algo = None
    type = None
    name = None
    supervised_algos = ['LinearRegression', 'DecisionTreeClassifier']
    unsupervised_algos = ['PCA']

    def __init__(self, algo):
        self.algo = algo
        self.name = self.algo.__class__.__name__
        if self.name in self.supervised_algos:
            self.type = 'supervised'
        elif self.name in self.unsupervised_algos:
            self.type = 'unsupervised'
        print('Initialising', self.name, '(', self.type, ')')

    def train(self, X, Y = None):
        # Input preprocessing
        X = np.asarray(X)

        if self.type == 'supervised':
            X = np.reshape(X, (-1, 1))

        # Train the model using the training sets
        if self.type == 'supervised':
            self.algo.fit(X, Y)
        elif self.type == 'unsupervised':
            self.algo.fit(X)

        #  Model persistence
        pickle.dump(self.algo, open('model.pk', 'wb')) #ml/model.pk model.pk

    def predict(self, X):
        # Input preprocessing
        X = np.asarray(X)

        if self.type == 'supervised':
            X = np.reshape(X, (-1, 1))

        # Load trained model from file
        self.algo = pickle.load(open('model.pk', 'rb')) #ml/model.pk model.pk

        # Model inference
        if self.type == 'supervised':
            Y = self.algo.predict(X)
        elif self.type == 'unsupervised':
            Y = self.algo.transform(X)

        return Y.tolist()

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
