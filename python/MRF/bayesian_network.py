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
