from multipledispatch import dispatch 
import matplotlib.pyplot as plt
import numpy as np

class Agent:
      
    def __init__(self, Granulator, Metric, external_extractor, Representative, obj_clustering):
        
        self.AgentExtractor = external_extractor
        self.Metric_Class = Metric # Classe Metric 
        self.obj_metric = Metric() # Oggetto di classe Metric 
        self.Representative_Class = Representative  # Classe Representative 
        self.obj_representative  = Representative() # Oggetto di classe Metric 
        self.obj_clustering = obj_clustering # Oggetto di classe Clustering
        self.Granulator_Class = Granulator # Classe Granulator
        
    def execute(self,S_T):
        self.Symbol_Threshold = S_T;
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator = self.Granulator_Class(self.obj_metric, self.obj_representative, self.obj_clustering, self.Symbol_Threshold) #Oggetto di classe Granulator
        self.AgentGranulator.Process(sample)
        
'''     
    @dispatch(int,float)     
    def execute(self, k_max, S_T):
        self.k_max=k_max
        self.Symbol_Threshold = S_T;
        self.obj_clustering = self.Clustering()
        self.obj_clustering.setup_clustering(k_max)
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator = self.Granulator_Class(self.obj_metric, self.obj_representative, self.obj_clustering) #Oggetto di classe Granulator
        self.AgentGranulator.Process(sample)
'''