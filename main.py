from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Granule import Granule
import matplotlib.pyplot as plt


m1 = Metric()
g1 = Granule()
x1 = Agent('iris_data.txt',"sepal width",0.1,4,m1.Diss)
x2 = Agent('iris_data.txt',"petal length",0.7,4,m1.Diss)

print("ClusteringParams_ID:") #Stampo ID dei granuli
print(x1.ClusteringParams_ID)

print("ClusteringParams values:") #Stampo valori dei granuli
print(x1.ClusteringParams_values)

g1.set_Representative(x1.Representatives[0]) #Set del valore Representative della classe Granulo
print("Representative_Granulo_0:")
print(g1.Representative)

print("Representatives:")
print(x1.Representatives)


