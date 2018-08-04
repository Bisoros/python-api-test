import ml.ml as ml #ml.ml as ml ml
from sklearn import linear_model

def init():
    algo = linear_model.LinearRegression()
    ml_object = ml.Ml(algo)
    return ml_object

'''
import linear_regression
object = linear_regression.init()
object.test_linear_regression()
object.predict(7)

# object.train(X, Y)
'''
