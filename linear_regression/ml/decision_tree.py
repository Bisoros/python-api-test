import ml.ml as ml #ml.ml as ml ml
from sklearn.tree import DecisionTreeClassifier

def init():
    algo = DecisionTreeClassifier(random_state=0)
    ml_object = ml.Ml(algo)
    return ml_object

'''
import decision_tree
object = decision_tree.init()
object.test_decision_tree()
# object.train(X, Y)
object.predict(X)
'''
