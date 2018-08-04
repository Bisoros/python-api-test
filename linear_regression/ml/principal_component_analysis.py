import ml
from sklearn import decomposition

def init():
    algo = decomposition.PCA(n_components = 2)
    ml_object = ml.Ml(algo)
    return ml_object

'''
import principal_component_analysis
object = principal_component_analysis.init()
object.predict(X)
'''
