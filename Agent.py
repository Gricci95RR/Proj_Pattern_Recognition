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
        self.obj_clustering = Clustering()
        
    def execute(self, theta, Q, S_T):
        self.Theta = theta;
        self.Lambda = Q; 
        self.Symbol_Threshold = S_T;
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator.Setup(self.Lambda, self.Theta, self.Symbol_Threshold,self.obj_metric, self.obj_representative, self.obj_clustering)
        self.AgentGranulator.Process(sample)
                       
    def get_Theta(self):
        return self.Theta
    
    def get_Lambda(self):
        return self.Lambda
    
    def get_ClusteringParams_ID(self):
        return self.ClusteringParams_ID
    
    def get_MetricParams(self):
        return self.MetricParams
    

