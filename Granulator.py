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
   
    def Process1(self,sample,diss):
        cardinalita = [];
        self.sample = sample;
        bsas_instance = bsas(self.sample, self.Lambda, self.Symbol_Threshold,diss)
        bsas_instance.process()
        # Get clustering results.
        clusters = bsas_instance.get_clusters()
        representatives = bsas_instance.get_representatives()
        bsas_visualizer.show_clusters(self.sample, clusters, representatives)
        
        # Calcolo cardinalità
        for i in range(0,len(clusters)):
            cardinalita.append(len(clusters[i]))
         
        # Creazione oggetto granulo
        granulo = Granule()
        # Set Params oggetto granulo
        granulo.set_Representative(representatives)
        granulo.set_Cardinality(cardinalita)
        # Inserimento in lista oggetto granulo
        self.lista_di_granuli.append(granulo)
        
        print('lista di granuli:')
        print(self.lista_di_granuli)
        print('cardinalità:')  
        print(cardinalita)
        print('clusters:')
        print(clusters)
        print('representatives:')
        print(representatives)
        return clusters, representatives
