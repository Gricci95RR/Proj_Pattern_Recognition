from pyclustering.cluster.bsas import bsas, bsas_visualizer
from pyclustering.utils import read_sample

class Granulator:
    def get_Symbol_Threshold(self):
        return self.Symbol_Threshold
    def get_Lambda(self):
        return self.Lambda
    def set_Symbol_Threshold(self,S_T):
        self.Symbol_Threshold = S_T
    def set_Lambda(self, L):
        self.Lambda = L
    def Process(self,sample,max_clusters, threshold,granule): #SpareBSAS
        bsas_instance = bsas(sample, max_clusters, threshold)
        bsas_instance.process()
        # Get clustering results.
        clusters = bsas_instance.get_clusters()
        representatives = bsas_instance.get_representatives()
        granule.set_Representative(representatives)
        bsas_visualizer.show_clusters(sample, clusters, representatives)
        print('clusters:')
        print(clusters)
        print('representatives:')
        print(representatives)
        return clusters, representatives
