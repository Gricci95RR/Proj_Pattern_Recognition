from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent
from Metric import Metric
from Representative import Representative
from Clustering_MBSAS import Clustering_MBSAS
from Clustering_K_Means import Clustering_K_Means

extractor1 = Extractor()

agent1 = Agent(Granulator, Metric, extractor1, Representative, Clustering_MBSAS)
agent1.execute(5, 3.0, 0.5, 0.5, 1.1) # Lambda, S_T, theta_start ,theta_step, theta_stop


agent2 = Agent(Granulator, Metric, extractor1, Representative, Clustering_K_Means)
agent2.execute(3, 3.1) # k_max, S_T
