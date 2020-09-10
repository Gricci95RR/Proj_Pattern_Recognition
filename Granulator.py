from pyclustering.cluster.bsas import bsas, bsas_visualizer
from Granule import Granule
import numpy
import itertools
import random
import matplotlib.pyplot as plt
from statistics import mean

class Granulator:
    lista_di_granuli = [];
    def get_Symbol_Threshold(self):
        return self.Symbol_Threshold
    def get_Lambda(self):
        return self.Lambda
    def set_Symbol_Threshold(self,S_T):
        self.Symbol_Threshold = S_T
    def set_Lambda(self, L):
        self.Lambda = L
    def Setup(self,L, S_T, obj_metric, obj_representative,obj_clustering_bsas):
        self.Lambda = L
        self.Symbol_Threshold = S_T
        self.obj_metric = obj_metric
        self.obj_representative = obj_representative 
        self.obj_clustering_bsas = obj_clustering_bsas
    
    def Process(self, dataset, obj_clustering_bsas):  # SpareBSAS
        self.obj_clustering_bsas.clustering_bsas(dataset,self.Lambda,self.Symbol_Threshold,self.obj_metric,self.obj_representative)
   

