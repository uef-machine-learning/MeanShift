__author__ = 'Jiawei yang'

#reference: 	J.W.Yang???S. Rahardja, and P. Fr??nti, "Mean-shift outlier detection," Int. Conf. Fuzzy Systems and Data Mining (FSDM), 2018.
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial import distance


class MS():
    def __init__(self,data,k):
             self.data=data
             self.k=k
             self.iteration_number = 3

    def getDst(self,data, data_shifted):
        j = 0
        dislist = []
        while (j <  len(data)):
            dst = np.sqrt(np.sum((data[j] - data_shifted[j]) ** 2))
            dislist.append(dst)
            j += 1
        return np.array(dislist)

    def k_nearest_neighbor(self,point, nbrs,points):
        distances, indices = nbrs.kneighbors([point])
        k_smallest = []
        for i,p in enumerate(indices[0]):
            k_smallest.append(points[p])
        # k_smallest.pop(0)
        del k_smallest[0]
        return k_smallest


    def get_medoid(self,coords):
        coords=np.array(coords)
        cost = distance.cdist(coords, coords, 'cityblock')# Manhattan distance,  'euclidean','minkowski'
        return coords[np.argmin(cost.sum(axis=0))]

    def get_mean(self,coords):
        return np.mean(coords, axis=0)

    def shift_iterationMean(self,points, k, iteration_number):
        shift_points = np.array(points)
        shift_points_COPY = shift_points[:]
        while(iteration_number>0):       #['auto', 'brute','kd_tree', 'ball_tree']

            nbrs = NearestNeighbors(n_neighbors=k,algorithm='auto').fit(shift_points_COPY)
            for i,point in enumerate(shift_points_COPY):
                KNearestNeighbor = self.k_nearest_neighbor(shift_points[i], nbrs,shift_points_COPY)
                shift_points[i] =self.get_mean(KNearestNeighbor)# mean or medoid
                iteration_number -= 1
            shift_points_COPY = shift_points[:]
        return  shift_points


    def shift_iterationMedoid(self,points, k, iteration_number):
        shift_points = np.array(points)
        shift_points_COPY = shift_points[:]
        while (iteration_number > 0):  # ['auto', 'brute','kd_tree', 'ball_tree']

            nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(shift_points_COPY)
            for i, point in enumerate(shift_points_COPY):
                KNearestNeighbor = self.k_nearest_neighbor(shift_points[i], nbrs, shift_points_COPY)
                shift_points[i] = self.get_medoid(KNearestNeighbor)  # mean or medoid
                iteration_number -= 1
            shift_points_COPY = shift_points[:]
        return shift_points

    def runMean(self):
        iteration=1
        result=self.data[:]
        while(iteration<=self.iteration_number):
             result = self.shift_iterationMean(result, self.k, 1)
             iteration +=1
        return self.getDst(self.data,result)

    def runMeanShift(self):
        iteration = 1
        result = self.data[:]
        while (iteration <= self.iteration_number):
            result = self.shift_iterationMean(result, self.k, 1)
            iteration += 1
        return result
    def runMedoidShift(self):
        iteration=1
        result=self.data[:]
        while(iteration<=self.iteration_number):
             result = self.shift_iterationMedoid(result, self.k, 1)
             iteration +=1
        return result

    def runMedoid(self):
        iteration=1
        result=self.data[:]
        while(iteration<=self.iteration_number):
             result = self.shift_iterationMedoid(result, self.k, 1)
             iteration +=1
        return self.getDst(self.data,result)

    def run(self):

        outlierscore_MOD=self.runMean()
        outlierscore_DOD=self.runMedoid()
        return outlierscore_MOD,outlierscore_DOD

