from Granulator import Granulator
from Extractor import Extractor
from Granule import Granule

class Agent:
    Symbol_Threshold = 0; 
    Labda = 0; #max num of clusters
    ClusteringParams_ID = 0; #list of clusters' pattern IDs
    MetricParams = 0;
    Representatives = 0; #list of clusters' medoids
    
    def __init__(self,name,nome_colonna,theta, Q,dissimilarityFunction):
        self.Symbol_Threshold = theta;
        self.Labda = Q; #__verifica__
        e = Extractor(); #dichiaro oggetto di tipo Extractor
        data_frame = e.Extract(name)
        colonna = data_frame[nome_colonna].tolist()
        g = Granulator(theta, Q); #dichiaro oggetto di tipo Granulator
        self.ClusteringParams_ID, self.Representatives = g.Process(colonna, theta, Q,dissimilarityFunction)
        
    def get_Symbol_Threshold(self):
        return self.Symbol_Threshold
    
    def get_Labda(self):
        return self.Labda
    
    def get_ClusteringParams_ID(self):
        return self.ClusteringParams_ID
    
    def get_MetricParams(self):
        return self.MetricParams
    
    #def Extract(self, name):
    #    e = Extractor(); #dichiaro oggetto di tipo Extractor
    #    data_frame = e.Extract('iris_data.txt')
    #    return data_frame
    #def Granulate(self, dataset, theta, Q, dissimilarityFunction):
    #    g = Granulator(); #dichiaro oggetto di tipo Granulator
    #    g.Process(dataset, theta, Q,dissimilarityFunction)

