from Granule import Granule
import matplotlib.pyplot as plt
from statistics import mean
from multipledispatch import dispatch 

class Granulator:
    lista_di_granuli = [];
    
    @dispatch(float,int,float,object,object,object)  
    def Setup(self, theta, L, S_T, obj_metric, obj_representative,obj_clustering):
        self.obj_metric = obj_metric
        self.obj_representative = obj_representative 
        self.obj_clustering = obj_clustering
        self.obj_clustering.setup_clustering(L,theta,S_T)
        
    @dispatch(int,object,object,object)  
    def Setup(self, n_c, obj_metric, obj_representative,obj_clustering):
        self.obj_metric = obj_metric
        self.obj_representative = obj_representative 
        self.obj_clustering = obj_clustering
        self.obj_clustering.setup_clustering(n_c)
    
    def Process(self, dataset):
        
        representatives, clusters_v = self.obj_clustering.clustering(dataset, self.obj_metric, self.obj_representative)
        
        
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
        
        Plot(representatives,cardinalita,clusters_v)
        
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
        print("Granuli")
        print(self.lista_di_granuli)
        print("Clusters_v")
        print(clusters_v)
        
        return representatives, clusters_v, self.lista_di_granuli
        
        
def Plot(representatives,cardinalita,clusters_v):
    # divido clusters values e representatives in due vettori e divido lista clusters_v e representatives in nested list
    x = []
    y = []
    x_r = []
    y_r = []
    for i in range(0,len(cardinalita)):
        x.append([])
        y.append([])
        x_r.append([])
        y_r.append([])
    # estraggo coordinate x e y dei representatives
    for i in range(0,len(representatives)):
        for j in range(0,len(representatives[i])):
            if j == 0:
                x_r[i].append(representatives[i][j])         
            else:
                y_r[i].append(representatives[i][j])
                        
        
    # estraggo coordinate x e y dei clusters
    x = []
    y = []
    for i in range(0,len(clusters_v)):
        x.append([])
        y.append([])
        for j in range(1,len(clusters_v[i])):
            for k in range(0,2):
                if k == 0:
                    x[i].append(clusters_v[i][j][k])         
                else:
                    y[i].append(clusters_v[i][j][k])
    #plot
    fig, ax = plt.subplots(1,figsize=(7,5))
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(0,len(cardinalita)):
        plt.scatter(x[i], y[i], s = 100)
        plt.scatter(x_r[i],y_r[i], marker='*' ,s = 100,c = 'yellow')
        
        
   

