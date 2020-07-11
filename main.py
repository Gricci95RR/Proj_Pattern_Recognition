from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric


metric1 = Metric()
metric1 = Metric()
extractor1 = Extractor()
granulator1 = Granulator()

agent1 = Agent(granulator1,extractor1,metric1)

agent1.execute(0.01,5)

metric2 = Metric()
metric2 = Metric()
extractor2 = Extractor()
granulator2 = Granulator()

agent2 = Agent(granulator1,extractor1,metric1)

agent1.execute(0.01,5)