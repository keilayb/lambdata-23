import numpy as np
import pandas as pd
from sklearn.utils import shuffle


class Data:
    def __init__(self, data):
        if type(data) == pd.core.series.Series:
            self.data = data
        elif type(data) == pd.core.arrays.numpy_.PandasArray:
            self.data = pd.Series(data)
        elif type(data) == list:
            self.data = pd.Series(data)
        elif (type(data) == str) & (".csv" in data):
            self.data = pd.read_csv(data)
        elif type(data) == pd.core.frame.DataFrame:
            self.data = data

    def null_count(self):
        if type(self.data) == pd.core.series.Series:
            df = pd.DataFrame(self.data)
        elif type(self.data) == pd.core.frame.DataFrame:
            df = self.data
        null_values = df.isnull().sum().sum()
        return null_values

    def randomize(self, seed=None):
        if type(self.data) == pd.core.series.Series:
            df = pd.DataFrame(self.data)
        if type(self.data) == pd.core.frame.DataFrame:
            df = self.data
        shuffle1 = shuffle(df, random_state=seed)
        cols = df.columns
        for col in cols:
            shuffle1[col] = np.random.permutation(shuffle1[col])
        return shuffle1


# Code to test whether functions work
# test_list = [228, 8902, 563, 2, 67]
# test_datalist = Data(test_list)
# print(test_datalist.randomize(2))
#
# test_df = pd.DataFrame({'A': [1, 2, 3, 4],
#                         'B': [5, 6, 7, 8],
#                         'C': [9, 10, 11, 12]})
#
# df_data = Data(test_df)
#
# # print(df_data.randomize(3))
