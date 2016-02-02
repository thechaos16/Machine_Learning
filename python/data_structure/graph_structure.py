# -*- coding: utf-8 -*-

import sys
import numpy as np
import scipy.sparse as sp

class Graph:
    def __init__(self,data,opt='matrix'):
        self.opt = opt
        if self.opt=='matrix':
            self.graph = self.graph_with_sparse_matrix(data)
        elif self.opt=='dict':
            self.graph = self.graph_with_dictionary(data)
        else:
            sys.exit('Error! you should specify type of representation!')
    
    ## dictionary
    ## format: {'A':[('B',3.3),('C',1.0)]}
    def graph_with_dictionary(self,data):
        data_connection = data['connection']
        try:
            data_weight = data['weight']
            if len(data_weight)!=len(data_connection):
                data_weight = np.ones(len(data_connection))
        except KeyError:
            data_weight = np.ones(len(data_connection))
        graph_dictionary = {}
        for i in range(len(data_connection)):
            tup = data_connection[i]
            try:
                graph_dictionary[tup[0]].append((tup[1],data_weight[i]))
            except KeyError:
                graph_dictionary[tup[0]] = [(tup[1],data_weight[i])]
            if not data['directed']:
                try:
                    graph_dictionary[tup[1]].append((tup[0],data_weight[i]))
                except KeyError:
                    graph_dictionary[tup[1]] = [(tup[0],data_weight[i])]
        return graph_dictionary
        
    ## matrix
    ## vertices should be numbered
    def graph_with_sparse_matrix(self,data):
        ## make full matrix
        data_connection = data['connection']
        try:
            data_weight = data['weight']
            if len(data_weight)!=len(data_connection):
                data_weight = np.ones(len(data_connection))
        except KeyError:
            data_weight = np.ones(len(data_connection))
        vertex_number = max([max(elm) for elm in data_connection])
        matrix_form = np.zeros((vertex_number,vertex_number))
        ## directed or undirected
        if data['directed']:
            for i in range(len(data_connection)):
                tup = data_connection[i]
                matrix_form[tup[0]-1][tup[1]-1]=data_weight[i]
        else:
            for i in range(len(data_connection)):
                tup = data_connection[i]
                matrix_form[tup[0]-1][tup[1]-1]=data_weight[i]
                matrix_form[tup[1]-1][tup[0]-1]=data_weight[i]
        ## make it sparse
        ## csr form
        return sp.csr_matrix(matrix_form)
        ## lil form
        #return sp.lil_matrix(matrix_form)
        
    ## return graph
    def get_graph(self):
        return self.graph
        
    ## show graph
    def show_graph(self):
        if self.opt=='matrix':
            print(self.graph.toarray())
        else:
            print(self.graph)

if __name__=='__main__':
    data = {'connection':[(1,2),(1,3),(1,4),(2,4),(4,5),(4,6),(5,6)],'directed':True}
    show_type = 'matrix'
    aa = Graph(data,show_type)
    graph = aa.get_graph()