from scipy.spatial import distance

class Metric:
    Weight_Params = [];
    def Diss(self,a, b):
        dst = distance.euclidean(a, b)
        return dst

