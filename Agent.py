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
        
        
    @dispatch(float,int,float)     
    def execute(self, theta, Q, S_T):
        self.Theta = theta;
        self.Lambda = Q; 
        self.Symbol_Threshold = S_T;
        self.obj_clustering.setup_clustering(Q,theta,S_T)
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator = self.Granulator_Class(self.obj_metric, self.obj_representative, self.obj_clustering) #Oggetto di classe Granulator
        self.AgentGranulator.Process(sample)
        
    
    @dispatch(int,float)     
    def execute(self, n_c, S_T):
        self.n_c=n_c
        self.Symbol_Threshold = S_T;
        self.obj_clustering = self.Clustering()
        self.obj_clustering.setup_clustering(n_c)
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator = self.Granulator_Class(self.obj_metric, self.obj_representative, self.obj_clustering) #Oggetto di classe Granulator
        self.AgentGranulator.Process(sample)
'''
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
    
    @dispatch(float,float)     
    def evaluate(self,theta_step,theta_stop):
        thetas = np.arange(0,theta_stop,theta_step)
        thetas2 = []
        for theta in thetas:
            self.obj_clustering = self.Clustering()
            sample = self.AgentExtractor.Extract('iris_data.txt')
            self.AgentGranulator.Setup(theta,self.Lambda, self.Symbol_Threshold, self.obj_metric, self.obj_representative, self.obj_clustering)
            representatives, points, lista_di_granuli = self.AgentGranulator.Process(sample) 
            if len(representatives) != self.Lambda:
                thetas2.append(theta)
        print('Lista di Theta',thetas2)
'''