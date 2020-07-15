from Extractor import Extractor
from Granulator import Granulator
from Agent import Agent

extractor1 = Extractor()

agent1 = Agent(Granulator,extractor1)

agent1.execute(0.1,5)



extractor2 = Extractor()

agent2 = Agent(Granulator,extractor1)

agent1.execute(0.3,5)