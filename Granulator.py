from pyclustering.cluster.bsas import bsas, bsas_visualizer

class Granulator:
    def get_Symbol_Threshold(self):
        return self.Symbol_Threshold
    def get_Lambda(self):
        return self.Lambda
    def set_Symbol_Threshold(self,S_T):
        self.Symbol_Threshold = S_T
    def set_Lambda(self, L):
        self.Lambda = L
    def Setup(self,L,S_T):
        self.Lambda = L
        self.Symbol_Threshold = S_T
        
    def Process(self,sample,granule):
        cardinalita = [];
        self.sample = sample;
        bsas_instance = bsas(self.sample, self.Lambda, self.Symbol_Threshold)
        bsas_instance.process()
        # Get clustering results.
        clusters = bsas_instance.get_clusters()
        representatives = bsas_instance.get_representatives()
        bsas_visualizer.show_clusters(self.sample, clusters, representatives)
        #calcolo cardinalità
        for i in range(0,len(clusters)):
            cardinalita.append(len(clusters[i]))
        #calcolo parametri classe Granule  
        granule.set_Representative(representatives)
        granule.set_Cardinality(cardinalita)
        
        print('cardinalità:')  
        print(cardinalita)
        print('clusters:')
        print(clusters)
        print('representatives:')
        print(representatives)
        return clusters, representatives
