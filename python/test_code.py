# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:10:32 2016

@author: minkyu
"""

import data_structure.graph_structure as gr
data = {'connection':[(1,2),(1,3),(1,4),(2,4),(4,5),(4,6),(5,6)],'directed':True}
show_type = 'matrix'
aa = gr.Graph(data,show_type)
graph = aa.get_graph()