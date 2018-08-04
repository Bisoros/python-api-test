import ml
from sklearn import decomposition

def init():
    algo = decomposition.PCA()
    ml_object = ml.Ml(algo)
    return ml_object

'''
import linear_regression
object = linear_regression.init()
# object.test_linear_regression()
object.train(X, Y)
object.predict(X)
'''
