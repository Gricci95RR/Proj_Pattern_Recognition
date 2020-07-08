import pandas as pd


class Extractor:
    def Extract(self, name):
        data=pd.read_csv(name, sep=",", header=None,names= ["sepal length", "sepal width" , "petal length", "petal width", "class"])
        data=data.sample(frac=0.5) #frac = fraction of rows to return in the random sample
        data=data.iloc[:, 1:4]
        return data
