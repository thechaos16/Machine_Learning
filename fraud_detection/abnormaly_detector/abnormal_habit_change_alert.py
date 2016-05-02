# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:36:02 2016

@author: minkyu
"""

import sys
import os
import pandas as pd
import numpy as np
try:
    import statistical_difference as sd
except ImportError:
    sys.path.append('../')
    import statistical_difference as sd
from abnormaly_detector.abnormal_performance_improvement_alert import PerformanceAlert
    

class HabitAlert(PerformanceAlert):
    def __init__(self, user_id, db_path, domain=None, opt={}):
        super().__init__(user_id, db_path, domain, opt)
    
    def abnormal_habit_change(self):
        extract_from_db = self.db[self.user_id]
    
    
if __name__ == '__main__':
    kk = HabitAlert('','')