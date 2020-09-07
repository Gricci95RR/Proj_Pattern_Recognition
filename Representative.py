from statistics import mean
import numpy
import itertools

class Representative:
    
    def Update_M(self,clusters,index_cluster,clusters_DissimMatrix,dataset,obj_metric):
                    D = numpy.zeros((len(clusters[index_cluster]), len(clusters[index_cluster])))
                    D[:-1, :-1] = clusters_DissimMatrix[index_cluster]
    
                    v_left, v_right = [], []
                    for j, k in itertools.product([D.shape[1] - 1], range(D.shape[0] - 1)):
                        v_left.append(
                            obj_metric.Diss(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][k]]))
                    for j, k in itertools.product(range(D.shape[1] - 1), [D.shape[0] - 1]):
                        v_right.append(
                            obj_metric.Diss(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][k]]))
                    v = 0.5 * (numpy.array(v_left) + numpy.array(v_right))
                    D[0:-1, -1] = v
                    D[-1, 0:-1] = v
                    minSOD_ID = numpy.argmin(numpy.sum(D, axis=1))
                    return minSOD_ID, D
       
    '''
    def Update(self,clusters_v,representatives):
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
            # __calcolo centroidi
            x_r_c=[]
            y_r_c=[]
            for i in range(0,len(x)):
                x_r_c.append([])
                y_r_c.append([])
                x_r_c[i]=mean(x[i])
                y_r_c[i]=mean(y[i])
            for i in range(0,len(x_r_c)):
                representatives[i][0]=x_r_c[i]
            for i in range(0,len(y_r_c)):
                representatives[i][1]=x_r_c[i] 
                
                return x_r_c, y_r_c, representatives
    
    '''   

