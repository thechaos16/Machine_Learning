# -*- coding: utf-8 -*-

import sys
import numpy as np
import scipy.sparse as sp

class Graph:
    def __init__(self,data,opt='matrix'):
        if opt=='matrix':
            self.graph = self.graphWithSparse(data)
        elif opt=='dict':
            self.graph = self.graphWithDict(data)
        else:
            sys.exit('Error! you should specify type of representation!')
    
    ## dictionary
    ## format: {'A':[('B',3.3),('C',1.0)]}
    def graphWithDict(self,data):
        dConnection = data['connection']
        try:
            dWeight = data['weight']
            if len(dWeight)!=len(dConnection):
                dWeight = np.ones(len(dConnection))
        except KeyError:
            dWeight = np.ones(len(dConnection))
        graphDict = {}
        for i in range(len(dConnection)):
            tup = dConnection[i]
            try:
                graphDict[tup[0]].append((tup[1],dWeight[i]))
            except KeyError:
                graphDict[tup[0]] = [(tup[1],dWeight[i])]
            if not data['directed']:
                try:
                    graphDict[tup[1]].append((tup[0],dWeight[i]))
                except KeyError:
                    graphDict[tup[1]] = [(tup[0],dWeight[i])]
        return graphDict
        
    ## matrix
    ## vertices should be numbered
    def graphWithSparse(self,data):
        ## make full matrix
        dConnection = data['connection']
        try:
            dWeight = data['weight']
            if len(dWeight)!=len(dConnection):
                dWeight = np.ones(len(dConnection))
        except KeyError:
            dWeight = np.ones(len(dConnection))
        numV = max([max(elm) for elm in dConnection])
        matrixForm = np.zeros((numV,numV))
        ## directed or undirected
        if data['directed']:
            for i in range(len(dConnection)):
                tup = dConnection[i]
                matrixForm[tup[0]-1][tup[1]-1]=dWeight[i]
        else:
            for i in range(len(dConnection)):
                tup = dConnection[i]
                matrixForm[tup[0]-1][tup[1]-1]=dWeight[i]
                matrixForm[tup[1]-1][tup[0]-1]=dWeight[i]
        ## make it sparse
        ## csr form
        return sp.csr_matrix(matrixForm)
        ## lil form
        #return sp.lil_matrix(matrixForm)

if __name__=='__main__':
    data = {'connection':[(1,2),(1,3),(1,4),(2,4),(4,5),(4,6),(5,6)],'directed':True}
    showType = 'matrix'
    aa = Graph(data,showType)