from scipy.spatial import distance

class Metric:
    Weight_Params = 0;
    def Diss(self,a, b):
        dst = distance.euclidean(a, b)
        return dst

