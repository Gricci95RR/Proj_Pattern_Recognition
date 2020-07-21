class Agent:
    #Symbol_Threshold 
    #Labda max num of clusters
      
    def __init__(self, Granulator, Metric, external_extractor):
        self.AgentGranulator = Granulator()
        self.AgentExtractor = external_extractor
        self.Metric_Class = Metric # Classe Metric in metodo Setup
        self.obj_metric = Metric() # Oggetto di classe Metric in metodo Setup
        self.Symbol_Threshold = 0;
        self.Lambda = 0; 
        
    def execute(self, theta, Q):
        self.Symbol_Threshold = theta;
        self.Lambda = Q; 
        sample = self.AgentExtractor.Extract('iris_data.txt')
        self.AgentGranulator.Setup(self.Lambda, self.Symbol_Threshold, self.obj_metric)
        self.AgentGranulator.Process(sample)
                       
    def get_Symbol_Threshold(self):
        return self.Symbol_Threshold
    
    def get_Lambda(self):
        return self.Lambda
    
    def get_ClusteringParams_ID(self):
        return self.ClusteringParams_ID
    
    def get_MetricParams(self):
        return self.MetricParams
    

