from multipledispatch import dispatch 
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
import numpy as np

class Agent:
      
    def __init__(self, Granulator, Metric, external_extractor, Representative, Clustering):
        self.AgentGranulator = Granulator()
        self.AgentExtractor = external_extractor
        self.Metric_Class = Metric # Classe Metric 
        self.obj_metric = Metric() # Oggetto di classe Metric 
        self.Representative_Class = Representative  # Classe Representative 
        self.obj_representative  = Representative() # Oggetto di classe Metric 
        self.Theta = 0;
        self.Lambda = 0; 
        self.Symbol_Threshold = 0;
        self.Clustering = Clustering
        
        
    @dispatch(float,int,float)     
    def execute(self, theta, Q, S_T):
        self.Theta = theta;
        self.Lambda = Q; 
        self.Symbol_Threshold = S_T;
        self.obj_clustering = self.Clustering()
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator.Setup(self.Theta,self.Lambda, self.Symbol_Threshold, self.obj_metric, self.obj_representative, self.obj_clustering)
        self.AgentGranulator.Process(sample)
    
    @dispatch(int,float)     
    def execute(self, n_c, S_T):
        self.n_c=n_c
        self.Symbol_Threshold = S_T;
        self.obj_clustering = self.Clustering()
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator.Setup(self.n_c, self.obj_metric, self.obj_representative, self.obj_clustering)
        self.AgentGranulator.Process(sample)
     
    @dispatch(int) 
    def evaluate(self,k_max):
        sse = []
        for k in range(1, k_max+1):
            
            self.obj_clustering = self.Clustering()
            sample = self.AgentExtractor.Extract('iris_data.txt')
            self.AgentGranulator.Setup(k, self.obj_metric, self.obj_representative, self.obj_clustering)
            centroids, points, lista_di_granuli = self.AgentGranulator.Process(sample)
    
            curr_sse = 0
                
            # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
            for i in range(len(points)): #num di cluster
                for j in range(0,len(points[i])): #num di punti per cluster
                    curr_center = centroids[i]
                    curr_sse += (points[i][j][0] - curr_center[0]) ** 2 + (points[i][j][1] - curr_center[1]) ** 2
            sse.append(curr_sse)
            
        fig = plt.figure()
        ax = plt.axes()
        x = np.arange(1, k_max+1,1)
        ax.plot(x, sse);
        ax.set_xlabel('K')
        ax.set_ylabel('Within-Cluster-Sum of Squared Errors')
        ax.set_title('Elbow Method') 