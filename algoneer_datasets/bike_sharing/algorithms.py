from typing import Dict, Any

from algoneer.algorithm.sklearn import SklearnAlgorithm
from algoneer.algorithm import Algorithm

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

algorithms : Dict[str, Any]= {
    'random-forest' : RandomForestRegressor,
    'logistic-regression' : LogisticRegression,
    'linear-regression' : LinearRegression,
    'k-nearest-neighbors' : KNeighborsClassifier,
    'decision-tree' : DecisionTreeClassifier,
    'gaussian-nb' : GaussianNB
}

def get_algorithm(type : str) -> Algorithm:
    return SklearnAlgorithm(algorithms[type]())
