from scipy.spatial import distance

class Metric:
    def __init__(self,Weight_Params):
        self.Weight_Params = Weight_Params
    def Diss(self,a, b):
        dst = distance.euclidean(a, b)
        return dst

