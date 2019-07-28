from . import load_dataset
from algoneer import DataSet
import pandas as pd

def test_loading():
    ds = load_dataset()
    assert isinstance(ds, DataSet)
    df = ds.df
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 32561
    assert len(df.columns) == 15