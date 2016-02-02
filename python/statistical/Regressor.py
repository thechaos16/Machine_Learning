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
        if 'alpha' in self.opt:
            alpha = self.opt['alpha']
        else:
            alpha = 1.0
        if 'l1_ratio' in self.opt:
            l1_ratio = self.opt['l1_ratio']
        else:
            l1_ratio = 0.5
        clf = lm.ElasticNet(alpha=alpha,l1_ratio=l1_ratio)
        clf.fit(self.X,self.Y)
        return clf.coef_
        
if __name__=='__main__':
    input_mat = np.array([np.sort(np.random.randn(100)),np.random.randn(100),np.random.randn(100)]).T
    output_mat = np.random.randn(100)
    sorted_output_mat = np.sort(output_mat)
    
    reg = Regressor(input_mat,output_mat)
    #reg = Regressor(input_mat,sorted_output_mat)    
    lin_coeff = reg.linear_regression()
    rid_coeff = reg.ridge_regression()
    lasso_coeff = reg.lasso()
    ela_coeff = reg.elastic_net()
    