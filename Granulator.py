from Granule import Granule
import matplotlib.pyplot as plt
from statistics import mean

class Granulator:
    lista_di_granuli = [];
    
    def __init__(self, obj_metric, obj_representative, obj_clustering):
        self.obj_metric = obj_metric
        self.obj_representative = obj_representative 
        self.obj_clustering = obj_clustering

    def Process(self, dataset):
        
        representatives, clusters_v = self.obj_clustering.evaluate(dataset, self.obj_metric, self.obj_representative)
        self.Add(representatives, clusters_v)
         
        '''
        print("Cardinalità")
        print(cardinalita)
        
        print("Distances")
        print(distanze)
        print("Compattezze")
        print(compattezza)
        print("Raggio")
        print(effective_Radius)
        print("Quality")
        print(quality)
        print("Clusters_v")
        print(clusters_v)
        '''
        print("Granuli")
        print(self.lista_di_granuli)
        
        return representatives, clusters_v, self.lista_di_granuli
    
    def Add(self,representatives,clusters_v):
        
        # Calcolo cardinalità
        cardinalita = []
        for i in range(0,len(clusters_v)):
            cardinalita.append(len(clusters_v[i]))
        
        # Assegno cardinalità
        # Creazione oggetto granulo
        granulo = Granule()
        # Set Params oggetto granulo
        granulo.set_Representative(representatives)
        granulo.set_Cardinality(cardinalita)
        
        # Calcolo distanze dei punti dei clusters dai loro rappresentanti
        distanze = []
        for i in range(0,len(representatives)):
            distanze.append([])
            for j in range(1,len(clusters_v[i])):
                distanza = self.obj_metric.Diss(clusters_v[i][j],representatives[i])
                distanze[i].append(distanza)
                
        # Calcolo compattezza
        compattezza = []
        for i in range(0,len(representatives)):
            somma = 0
            end = len(distanze[i])-1
            for j in range(0,len(distanze[i])):
                somma = somma + distanze[i][j] # Somma di tutte le distanze di un cluster
                if j == end:
                    compattezza.append(somma)
        # Set di compattezza
        granulo.set_Compactness(compattezza)
        
        # Calcolo Effective Radius
        effective_Radius = []
        for i in range(0, len(cardinalita)):
            avg = mean(distanze[i])
            effective_Radius.append(avg)    
        # Set Effective Radius
        granulo.set_Compactness(effective_Radius)
        
        # Calcolo Quality (valor medio di compattezza e cardinalità)
        quality = []
        for i in range(0, len(cardinalita)):
            avg2 = (compattezza[i]+cardinalita[i])/2 
            quality.append(avg2)
        # Set Quality
        granulo.set_Quality(quality)
        
        # Inserimento in lista oggetto granulo
        self.lista_di_granuli.append(granulo)

    
       
    
        

