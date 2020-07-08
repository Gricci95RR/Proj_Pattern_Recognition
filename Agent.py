from Granulator import Granulator
from Extractor import Extractor

class Agent:
    Symbol_Threshold = 0;
    Labda = 0;
    ClusteringParams = 0;
    MetricParams = 0;
    def Extract(self, name):
        e = Extractor(); #dichiaro oggetto di tipo Extractor
        data_frame = e.Extract('iris_data.txt')
        return data_frame
    def Granulate(self, dataset, theta, Q, dissimilarityFunction):
        g = Granulator(); #dichiaro oggetto di tipo Granulator
        g.Process(dataset, theta, Q,dissimilarityFunction)

