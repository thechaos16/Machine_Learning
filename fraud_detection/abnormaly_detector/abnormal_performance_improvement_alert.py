# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:13:46 2016

@author: minkyu
"""

class PerformanceAlert():
    def __init__(self, user_id, db_path, domain, opt = {}):
        self.user_id = user_id
        self.db_path = db_path
        self.domain = domain
        self.opt = opt
        
    ## firstly, figure out how to build database
    def __read_database(self):
        pass
    
    ## performance is defined differently along domain
    def abnormal_peformance_change(self):
        pass
    
    ## habit is defined differently along domain
    def abnormal_habit_change(self):
        pass
    


if __name__ == '__main__':
    pass