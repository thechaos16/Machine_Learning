# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:13:46 2016

@author: minkyu
"""

import sys
import os
import pandas as pd
try:
    import statistical_difference as sd
except ImportError:
    sys.path.append('../')
    import statistical_difference as sd

class PerformanceAlert():
    def __init__(self, user_id, db_path, domain, opt = {}):
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
        return db
    
    ## performance is defined differently along domain
    def abnormal_peformance_change(self, player_id):
        # first draft: one-dimensional performance
        extract_from_db = self.db[player_id]
    
    ## habit is defined differently along domain
    def abnormal_habit_change(self):
        pass


if __name__ == '__main__':
    pass