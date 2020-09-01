from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Representative import Representative

extractor1 = Extractor()

agent1 = Agent(Granulator, Metric, extractor1, Representative)

agent1.execute(0.1,4)