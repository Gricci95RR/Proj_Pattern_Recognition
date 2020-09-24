from multipledispatch import dispatch 
import matplotlib.pyplot as plt
import numpy as np

class Agent:
      
    def __init__(self, Granulator, Metric, external_extractor, Representative, Clustering):
        
        self.AgentExtractor = external_extractor
        self.Metric_Class = Metric # Classe Metric 
        self.obj_metric = Metric() # Oggetto di classe Metric 
        self.Representative_Class = Representative  # Classe Representative 
        self.obj_representative  = Representative() # Oggetto di classe Metric 
        self.Clustering = Clustering # Classe Clustering
        self.obj_clustering = self.Clustering() # Oggetto di classe Clustering
        self.Granulator_Class = Granulator # Classe Granulator
        
        
    @dispatch(float,int,float,float,float)     
    def execute(self,Theta ,Q, S_T,theta_step,theta_stop):
        self.Theta = Theta;
        self.Lambda = Q; 
        self.Symbol_Threshold = S_T;
        self.theta_stop, self.theta_step = theta_stop,theta_step
        self.obj_clustering.setup_clustering(Theta,Q,S_T,theta_stop,theta_step)
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator = self.Granulator_Class(self.obj_metric, self.obj_representative, self.obj_clustering) #Oggetto di classe Granulator
        self.AgentGranulator.Process(sample)
        
    
    @dispatch(int,int,float)     
    def execute(self, k_max, k, S_T):
        self.k_max=k_max
        self.k=k
        self.Symbol_Threshold = S_T;
        self.obj_clustering = self.Clustering()
        self.obj_clustering.setup_clustering(k_max,k)
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator = self.Granulator_Class(self.obj_metric, self.obj_representative, self.obj_clustering) #Oggetto di classe Granulator
        self.AgentGranulator.Process(sample)
