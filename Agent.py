from multipledispatch import dispatch 

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
    def execute(self, n_c,S_T):
        self.n_c=n_c
        self.Symbol_Threshold = S_T;
        self.obj_clustering = self.Clustering()
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator.Setup(self.n_c, self.obj_metric, self.obj_representative, self.obj_clustering)
        self.AgentGranulator.Process(sample)
        