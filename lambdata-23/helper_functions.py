import pandas as pd


class Data:
    def __init__(self, data):
        if type(data) == pd.core.series.Series:
            self.data = data
        elif type(data) == pd.core.arrays.numpy_.PandasArray:
            self.data = pd.Series(data)
        elif type(data) == list:
            self.data = pd.Series(data)
        elif (type(data) == string) & (".csv" in data):
            self.data = pd.read_csv(data)

    def null_count(self):
        if type(self.data) == pd.core.series.Series:
            df = pd.DataFrame({"data": self.data})
        elif type(self.data) == pd.core.frame.DataFrame:
            df = self.data
        null_values = df.isnull().sum().sum()
        return null_values

    def randomize(self, seed):
        # if type(self.data) == pd.core.series.Series:
        #
        # if type(self.data) == pd.core.frame.DataFrame:
        #
        # return df
        pass


# Code to test whether functions work
# test_list = [228, 8902, 563, 2, 67]
# test_datalist = Data(test_list)
# print(test_datalist.data)
