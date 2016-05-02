# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:13:46 2016

@author: minkyu
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
try:
    import statistical_difference as sd
except ImportError:
    sys.path.append('../')
    import statistical_difference as sd

class PerformanceAlert:
    def __init__(self, user_id, db_path, domain=None, opt={}):
        self.user_id = user_id
        self.db_path = db_path
        self.db = self.__read_database()
        self.domain = self.__get_domain_knowledge(domain)
        self.opt = opt

    ## set specific domain knowledge
    def __get_domain_knowledge(self, domain):
        return        
    
    ## firstly, figure out how to build database
    def __read_database(self):
        # initialize DB variable
        db = pd.DataFrame([])
        # extract data from db
        # for test, make a fake data
        np.random.seed(42)
        random_series = pd.Series(np.random.random(size=10000))
        random_series[:5000]+=3.0
        # plt.figure()
        # plt.plot(random_series)
        db['player_id'] = random_series
        return db
    
    ## performance is defined differently along domain
    def abnormal_performance_change(self, player_id):
        # first draft: one-dimensional performance
        extract_from_db = self.db[player_id]
        aa = sd.difference_by_gradient(extract_from_db)
        print(aa)


if __name__ == '__main__':
    kk = PerformanceAlert('','')
    kk.abnormal_performance_change('player_id')
