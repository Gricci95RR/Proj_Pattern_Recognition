from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Representative import Representative
from Clustering import Clustering

extractor1 = Extractor()

agent1 = Agent(Granulator, Metric, extractor1, Representative, Clustering)

agent1.execute(0.1,4,3)