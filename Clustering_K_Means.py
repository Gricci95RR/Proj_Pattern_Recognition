import numpy as np
import pandas as pd

class Clustering_K_Means:
    def __init__(self ,k = 8, max_iter = 100 ):
        self.k = k
        self.max_iter = max_iter
        print("Initalized k with :",k)
        
    def setup_clustering(self, n_c):
        self.k = n_c # numero di cluster
    
    def fit(self, data,obj_metric, obj_representative):
        self.centroids = []
        #initialize the centroids, the first 'k' elements in the dataset will be our initial centroids
        for i in range(self.k):
            self.centroids.append(data.iloc[i].to_numpy())
            
        for itr in range(self.max_iter):
            self.classes = {}
            
            for cluster in range(self.k):
                self.classes[cluster] = []
                
    
            #find the distance between the point and cluster; choose the nearest centroid
            for point in range(len(data)):
                distances = obj_metric.Diss2(self.centroids, data.iloc[point].to_numpy())
                classification = np.argmin(distances)
                self.classes[classification].append(data.iloc[point])
                
            previous = np.array(self.centroids)
            #average the cluster datapoints to re-calculate the centroids
            for classification in self.classes:
                self.centroids[classification] = obj_representative.update_c(self.classes,classification)
            
            optimal = True
            curr = np.array(self.centroids)
        
            #difference in the cluster centers of two consecutive iterations to declare convergence.
            if np.sum((curr - previous)/previous * 100.0) > 0.0001:
                optimal = False
                
    def clustering(self,data,obj_metric, obj_representative):
        clf = Clustering_K_Means(self.k)
        data = pd.DataFrame(data)
        clf.fit(data,obj_metric,obj_representative)
        centroidi = clf.centroids
        clusters_v=[]
        i=0
        for classification in clf.classes:
            clusters_v.append([])
            for features in clf.classes[classification]:
                clusters_v[i].append(features[0])
                clusters_v[i].append(features[1])
            i=i+1

        n = 2 
        for j in range(0,len(clusters_v)):
            clusters_v[j] = [clusters_v[j][i * n:(i + 1) * n] for i in range((len(clusters_v[j]) + n - 1) // n )]
        print('ok')
        for k in range(0,len(centroidi)):
            centroidi[k]=centroidi[k].tolist()
            
        return centroidi, clusters_v 
    

