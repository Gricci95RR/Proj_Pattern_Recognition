from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Granule import Granule
import matplotlib.pyplot as plt

metric1 = Metric()
granule1 = Granule()
metric1 = Metric()
extractor1 = Extractor()
dati = extractor1.Extract('iris_data.txt')
granulator1 = Granulator()
agent1 = Agent(0.1,4)

agent1.Granulate(granulator1,dati,agent1.get_Labda(),agent1.get_Symbol_Threshold(),granule1)