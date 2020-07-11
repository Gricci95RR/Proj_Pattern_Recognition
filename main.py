from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric


metric1 = Metric()
metric1 = Metric()
extractor1 = Extractor()


agent1 = Agent(Granulator,extractor1,metric1)

agent1.execute(0.01,5)

metric2 = Metric()
metric2 = Metric()
extractor2 = Extractor()

agent2 = Agent(Granulator,extractor1,metric1)

agent1.execute(0.01,5)