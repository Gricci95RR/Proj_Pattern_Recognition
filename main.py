from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric

x1 = Agent()
df=x1.Extract('iris_data.txt')
print(df)

m1 = Metric()
sepal_width_list=df["sepal width"].tolist()
x1.Granulate(sepal_width_list,0.5, 5,m1.Diss)


