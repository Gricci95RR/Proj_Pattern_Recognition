from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Representative import Representative
from Clustering_MBSAS import Clustering_MBSAS
from Clustering_BSAS import Clustering_BSAS

extractor1 = Extractor()

agent1 = Agent(Granulator, Metric, extractor1, Representative, Clustering_MBSAS)

agent1.execute(0.1,4,3)

agent2 = Agent(Granulator, Metric, extractor1, Representative, Clustering_BSAS)

agent2.execute(0.4,4,3)