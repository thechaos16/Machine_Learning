# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:42:27 2016

@author: minkyu
"""

import numpy as np
import sklearn.linear_model as lm

class Regressor:
    def __init__(self,X,Y,opt={}):
        self.X = X
        self.Y = Y
        self.opt = opt
    
    def linear_regression(self):
        clf = lm.LinearRegression()
        clf.fit(self.X,self.Y)
        return clf.coef_
        
    def ridge_regression(self):
        clf = lm.Ridge(alpha=1.0)
        clf.fit(self.X,self.Y)
        return clf.coef_
        
    def lasso(self):
        try:
            alpha = self.opt['alpha']
        except KeyError:
            alpha = 0.1
        clf = lm.Lasso(alpha=alpha)
        clf.fit(self.X,self.Y)
        return clf.coef_
        
    def elastic_net(self):
        try:
            alpha = self.opt['alpha']
        except KeyError:
            alpha = 1.0
        clf = lm.ElasticNet(alpha=alpha)
        clf.fit(self.X,self.Y)
        return clf.coef_
        
if __name__=='__main__':
    input_mat = np.array([np.random.randn(100),np.random.randn(100),np.random.randn(100)]).T
    output_mat = np.random.randn(100)
    
    reg = Regressor(input_mat,output_mat)
    lin_coeff = reg.linear_regression()
    rid_coeff = reg.ridge_regression()
    lasso_coeff = reg.lasso()
    ela_coeff = reg.elastic_net()
    