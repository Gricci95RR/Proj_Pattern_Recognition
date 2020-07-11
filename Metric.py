from scipy.spatial import distance

class Metric:
    
    def Diss(self,a, b):
        dst = distance.euclidean(a, b)
        return dst

