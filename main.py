from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Granule import Granule

metric1 = Metric()
granule1 = Granule()
metric1 = Metric()
extractor1 = Extractor()
granulator1 = Granulator()

agent1 = Agent(granulator1,extractor1,metric1,granule1)
agent1.execute(0.1,4)

#agent1.Granulate(granulator1,dati,agent1.get_Lambda(),agent1.get_Symbol_Threshold(),granule1)

