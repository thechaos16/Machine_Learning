# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:48:17 2016

@author: minkyu
"""

import sys
try:
    import abnormaly_detector.abnormal_performance_improvement_alert as p_alert
except ImportError:
    sys.path.append('../')
    import abnormaly_detector.abnormal_performance_improvement_alert as p_alert
    

class FraudDetector():
    def __init__(self, user_id, db_path, domain):
        self.user_id = user_id
        self.db_path = db_path
        self.domain = domain
        
    # using abnormal performance alert module
    def abnormaly_detect(self):
        performance_alert = p_alert.PerformanceAlert(self.user_id, self.db_path, self.domain)
        
    # using deep learning?
    def fraud_detection_by_deep_learning(self):
        pass


if __name__ == '__main__':
    pass
