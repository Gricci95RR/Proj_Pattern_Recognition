from pyclustering.cluster.bsas import bsas, bsas_visualizer
from Granule import Granule
import numpy
import itertools
import random
import matplotlib.pyplot as plt
from statistics import mean

class Clustering_BSAS:
    lista_di_granuli = [];
    def clustering_bsas(self, dataset,Lambda,Symbol_Threshold,obj_metric,obj_representative,obj_clustering_bsas):
          
        """ Modified two-pass BSAS with approximate medoid tracking from the SPARE library
        Input:
        - dataset: list of items to be processed
        - theta: real-valued dissimilarity threshold for pattern inclusion
        - Q: maximum number of allowed clusters
        - dissimilarityFunction: callable for the dissimilarity measure to be used
        Output:
        - clusters: list of clusters' pattern IDs
        - clusters_v: list of clusters' pattern values
        - representatives: list of clusters' medoids
        - representatives_IDs: list of clusters' medoid IDs
        - clusters_DissimMatrix: list of clusters' dissimilarity matrices 
        - x: x coordinates of points of the clusters
        - y: y coordinates of points of the clusters.
        - x_r: x coordinates of points of the clusters' representatives
        - y_r: y coordinates of points of the clusters' representatives."""
        
        Q = Lambda;
        theta = Symbol_Threshold;
        # Set useful parameters
        poolSize = 20
    
        # Misc
        isAssigned = [False] * len(dataset)
    
        # First Round
        clusters = [[0]]  # first pattern
        clusters_v = [[0]]
        representatives = [dataset[0]]  # is
        representatives_IDs = [0]  # first cluster
        isAssigned[0] = True  #
    
        for i in range(1, len(dataset)):
            # grab current point
            point = dataset[i]
            # find distances w.r.t. all clusters
            distances = [obj_metric.Diss(point, medoid) for medoid in representatives]
            index_cluster = numpy.argmin(distances) 
            distance = distances[index_cluster]
    
            if distance > theta and len(clusters) < Q:
                representatives.append(point)
                clusters.append([i])
                clusters_v.append([i])
                representatives_IDs.append(i)
                isAssigned[i] = True
            else:
                pass
    
        # Second Round
        clusters_DissimMatrix = [numpy.zeros((1, 1))] * len(clusters)
        
        for i in range(0, len(dataset)):
            if isAssigned[i] is False:
                # grab current point
                point = dataset[i]
                # find distances w.r.t. all clusters
                distances = [obj_metric.Diss(point, medoid) for medoid in representatives]
                index_cluster = numpy.argmin(distances)
                distance = distances[index_cluster]
                # update medoid
                if len(clusters[index_cluster]) < poolSize:
                    clusters[index_cluster].append(i)
                    clusters_v[index_cluster].append(point)
                    minSOD_ID, D = obj_representative.Update_M(clusters,index_cluster,clusters_DissimMatrix,dataset,obj_metric)
            
                else:
                    id_pattern1, id_pattern2 = random.sample(range(0, poolSize), 2)
                    id_medoid = clusters[index_cluster].index(representatives_IDs[index_cluster])
                    
                    D = clusters_DissimMatrix[index_cluster]
                    d1 = D[id_medoid, id_pattern1]
                    d2 = D[id_medoid, id_pattern2]
                    if d1 >= d2:
                        toBeChanged = id_pattern1
                    else:
                        toBeChanged = id_pattern2
                    clusters[index_cluster][toBeChanged] = i
                    v_left, v_right = numpy.zeros(len(clusters[index_cluster])), numpy.zeros(len(clusters[index_cluster]))
                    for j in numpy.setdiff1d(range(len(clusters[index_cluster])), toBeChanged):
                        v_right[j] = obj_metric.Diss(dataset[clusters[index_cluster][j]],
                                                           dataset[clusters[index_cluster][toBeChanged]])
                        v_left[j] = obj_metric.Diss(dataset[clusters[index_cluster][toBeChanged]],
                                                          dataset[clusters[index_cluster][j]])
                    v = 0.5 * (v_left + v_right)
                    D[:, toBeChanged] = v
                    D[toBeChanged, :] = v
                    minSOD_ID = numpy.argmin(numpy.sum(D, axis=1))
                clusters_DissimMatrix[index_cluster] = D
                representatives[index_cluster] = dataset[clusters[index_cluster][minSOD_ID]]
                representatives_IDs[index_cluster] = clusters[index_cluster][minSOD_ID]
                
        # Calcolo cardinalità
        cardinalita = []
        for i in range(0,len(clusters)):
            cardinalita.append(len(clusters[i]))
        
        # Assegno cardinalità
        # Creazione oggetto granulo
        granulo = Granule()
        # Set Params oggetto granulo
        granulo.set_Representative(representatives)
        granulo.set_Cardinality(cardinalita)
        
        
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
            #plt.scatter(x_r_c[i], y_r_c[i], marker='*' ,s = 100,c = 'red') #__plot centroidi
        
        # Calcolo distanze dei punti dei clusters dai loro rappresentanti
        distanze = []
        for i in range(0,len(representatives)):
            distanze.append([])
            for j in range(1,len(clusters_v[i])):
                distanza = obj_metric.Diss(clusters_v[i][j],representatives[i])
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
        
        # Inserimento in lista oggetto granulo
        self.lista_di_granuli.append(granulo)
        return clusters, representatives, clusters_v, cardinalita, x, y, x_r, y_r  # , representatives_IDs, clusters_DissimMatrix 
