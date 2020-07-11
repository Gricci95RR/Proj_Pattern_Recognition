from Granulator import Granulator
from Extractor import Extractor
from Granule import Granule

class Agent:
    #Symbol_Threshold 
    #Labda max num of clusters
    
    def __init__(self,theta, Q):
        self.Symbol_Threshold = theta;
        self.Lambda = Q; 
        
    def Granulate(self, obj_granulator,sample,max_clusters, threshold, granule):
        obj_granulator.Process(sample, max_clusters, threshold, granule)
              
    def get_Symbol_Threshold(self):
        return self.Symbol_Threshold
    
    def get_Lambda(self):
        return self.Lambda
    
    def get_ClusteringParams_ID(self):
        return self.ClusteringParams_ID
    
    def get_MetricParams(self):
        return self.MetricParams
    

