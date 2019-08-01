from algoneer.dataset.pandas import PandasDataSet
import os

path = os.path.dirname(__file__)

def load_dataset():
    ds = PandasDataSet.from_path(path)
    return ds
