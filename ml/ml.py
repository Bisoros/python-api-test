from sklearn import linear_model
import pickle

def predict(X):
    clf = pickle.loads(s)
    prediction = clf.predict(X)
    return prediction
