# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:25:02 2016

@author: minkyu
"""

import os,sys
try:
    import data_structure.graph_structure as gr
except ImportError:
    sys.path.append(os.path.join(os.getcwd(),'../'))
    import data_structure.graph_structure as gr

## bayespy
## reference: https://github.com/bayespy/bayespy
import bayespy as bp
import bayespy.nodes as node


class BayesianNetwork():
    def __init__(self,graph_instance):
        ## if it is instance
        if isinstance(graph_instance,gr.Graph):
            self.graph = graph_instance.get_graph()
        ## if it is just data
        else:
            self.graph = gr.Graph(graph_instance,opt='matrix').get_graph()
            
    def get_graph(self):
        return self.graph
        
    def update_graph(self):
        pass        
        
    def message_passing(self):
        pass
        
        
if __name__=='__main__':
    data = {'connection':[(1,2),(1,3),(1,4),(2,4),(4,5),(4,6),(5,6)],'directed':True}
    show_type = 'matrix'
    aa = gr.Graph(data,show_type)
    bni = BayesianNetwork(data)
    graph = bni.get_graph()
    
    ## bayespy example
    mu = node.Gaussian([0, 0], [[1e-6, 0],[0, 1e-6]])
    Lambda = node.Wishart(2, [[1, 0], [0, 1]])
    X = Gaussian(mu, Lambda)
    X.show()