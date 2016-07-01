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
    def __init__(self, user_id, db_path, domain=None, opt={'time': 'year'}):
        self.user_id = user_id
        self.db_path = db_path
        self.opt = opt
        self.original_db = self.__read_database()
        self.time_series = self.__convert_data_into_time_series()
        self.domain = self.__get_domain_knowledge(domain)

    ## set specific domain knowledge
    def __get_domain_knowledge(self, domain):
        return        
    
    ## firstly, figure out how to build database
    def __read_database(self):
        # initialize DB variable
        db = pd.read_csv(self.db_path)
        return db

    # convert normal data into time-series data
    def __convert_data_into_time_series(self):
        fields = list(self.original_db.columns)
        user_id_idx = fields.index(self.user_id)
        time_field_idx = fields.index(self.opt['time'])
        db_dict = {}
        for line in self.original_db.values:
            id_data = line[user_id_idx]
            time = line[time_field_idx]
            if id_data not in db_dict:
                db_dict[id_data] = {}
            db_dict[id_data][time] = {fields[idx]: line[idx] for idx in range(len(line)) if fields[idx] != self.user_id and fields[idx] != self.opt['time']}            
        return db_dict
        
        
    ## performance is defined differently along domain
    def abnormal_performance_change(self, player_id):
        # first draft: one-dimensional performance
        extract_from_db = self.time_series[player_id]
        aa = sd.difference_by_gradient(extract_from_db)
        print(aa)


if __name__ == '__main__':
    kk = PerformanceAlert('player_id','../data/batting.csv')
    # kk.abnormal_performance_change('player_id')
