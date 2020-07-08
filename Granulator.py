import numpy
import itertools
import random
# import copy
from scipy.sparse import coo_matrix, dok_matrix
class Granulator:
    Symbol_Threshold = 0;
    Lambda = 0;
    def Process(self,dataset, theta, Q, dissimilarityFunction): #SpareBSAS
        """ Modified two-pass BSAS with approximate medoid tracking from the SPARE library

        Input:
        - dataset: list of items to be processed
        - theta: real-valued dissimilarity threshold for pattern inclusion
        - Q: maximum number of allowed clusters
        - dissimilarityFunction: callable for the dissimilarity measure to be used
        Output:
        - clusters: list of clusters' pattern IDs
        - representatives: list of clusters' medoids
        - representatives_IDs: list of clusters' medoid IDs
        - clusters_DissimMatrix: list of clusters' dissimilarity matrices. """
        # Set useful parameters
        poolSize = 20

        # Misc
        isAssigned = [False] * len(dataset)

        # First Round
        clusters = [[0]]                    # first pattern
        representatives = [dataset[0]]      # is
        representatives_IDs = [0]           # first cluster
        isAssigned[0] = True                #

        for i in range(1, len(dataset)):
            # grab current point
            point = dataset[i]

            # find distances w.r.t. all clusters
            distances = [dissimilarityFunction(point, medoid) for medoid in representatives]
            index_cluster = numpy.argmin(distances)
            distance = distances[index_cluster]

            if distance > theta and len(clusters) < Q:
                representatives.append(point)
                clusters.append([i])
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
                distances = [dissimilarityFunction(point, medoid) for medoid in representatives]
                index_cluster = numpy.argmin(distances)
                distance = distances[index_cluster]
                # update medoid
                if len(clusters[index_cluster]) < poolSize:
                    clusters[index_cluster].append(i)

                    D = numpy.zeros((len(clusters[index_cluster]), len(clusters[index_cluster])))
                    D[:-1, :-1] = clusters_DissimMatrix[index_cluster]

                    v_left, v_right = [], []
                    for j, k in itertools.product([D.shape[1] - 1], range(D.shape[0] - 1)):
                        v_left.append(dissimilarityFunction(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][k]]))
                    for j, k in itertools.product(range(D.shape[1] - 1), [D.shape[0] - 1]):
                        v_right.append(dissimilarityFunction(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][k]]))
                    v = 0.5 * (numpy.array(v_left) + numpy.array(v_right))
                    D[0:-1, -1] = v
                    D[-1, 0:-1] = v
                    minSOD_ID = numpy.argmin(numpy.sum(D, axis=1))
                else:
                    id_pattern1, id_pattern2 = random.sample(range(0, poolSize), 2)
                    id_medoid = clusters[index_cluster].index(representatives_IDs[index_cluster])
                    # old_D = clusters_DissimMatrix[index_cluster]
                    # d1 = old_D[id_medoid, id_pattern1]
                    # d2 = old_D[id_medoid, id_pattern2]
                    # if d1 >= d2:
                    #     old_D = numpy.delete(old_D, (id_pattern1), axis=0)
                    #     old_D = numpy.delete(old_D, (id_pattern1), axis=1)
                    #     del clusters[index_cluster][id_pattern1]
                    # else:
                    #     old_D = numpy.delete(old_D, (id_pattern2), axis=0)
                    #     old_D = numpy.delete(old_D, (id_pattern2), axis=1)
                    #     del clusters[index_cluster][id_pattern2]
                    # clusters[index_cluster].append(i)
                    # D = numpy.zeros((len(clusters[index_cluster]), len(clusters[index_cluster])))
                    # D[:-1, :-1] = old_D
                    # v_left, v_right = [], []
                    # for j, k in itertools.product([D.shape[1] - 1], range(D.shape[0] - 1)):
                    #     v_left.append(dissimilarityFunction(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][k]]))
                    # for j, k in itertools.product(range(D.shape[1] - 1), [D.shape[0] - 1]):
                    #     v_right.append(dissimilarityFunction(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][k]]))
                    # v = 0.5 * (numpy.array(v_left) + numpy.array(v_right))
                    # D[0:-1, -1] = v
                    # D[-1, 0:-1] = v
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
                        v_right[j] = dissimilarityFunction(dataset[clusters[index_cluster][j]], dataset[clusters[index_cluster][toBeChanged]])
                        v_left[j] = dissimilarityFunction(dataset[clusters[index_cluster][toBeChanged]], dataset[clusters[index_cluster][j]])
                    v = 0.5 * (v_left + v_right)
                    D[:, toBeChanged] = v
                    D[toBeChanged, :] = v
                    minSOD_ID = numpy.argmin(numpy.sum(D, axis=1))
                clusters_DissimMatrix[index_cluster] = D
                representatives[index_cluster] = dataset[clusters[index_cluster][minSOD_ID]]
                representatives_IDs[index_cluster] = clusters[index_cluster][minSOD_ID]
        
        print("clusters:")
        print(clusters)
        print("representatives:")
        print(representatives)
        print("representatives_IDs")
        print(representatives_IDs)
        print("clusters_DissimMatrix")
        print(clusters_DissimMatrix)
        
        return clusters, representatives, representatives_IDs, clusters_DissimMatrix
