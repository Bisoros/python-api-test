import .ml
from sklearn import linear_model

def init():
    algo = linear_model.LinearRegression()
    ml_object = ml.Ml(algo)
    return ml_object

'''
import linear_regression as lg
object = lg.init()
object.train(X, Y)
object.predict(X)
'''
