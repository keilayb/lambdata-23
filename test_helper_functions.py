import pandas as pd
import pytest
from lambdata_keilayb.helper_functions import Data

@pytest.fixture
def test_df():
    '''Returns a (4, 3) DataFrame'''
    df = pd.DataFrame({'A': [1, 2, 3, 4],
                       'B': [5, 6, 7, 8],
                       'C': [9, 10, 11, 12]})
    test_df = Data(df)
    return test_df

@pytest.fixture
def test_list():
    '''Returns a list of length 5'''
    list_= [228, 8902, 563, 2, 67]
    test_list = Data(list_)
    return test_list

# def test_null_count():
