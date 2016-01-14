# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:42:27 2016

@author: minkyu
"""

import numpy as np
import sklearn.linear_model as lm

class Regressor:
    def __init__(self,X,Y,opt=None):
        self.X = X
        self.Y = Y
        self.opt = opt
    
    def linearRegression(self):
        clf = lm.LinearRegression()
        clf.fit(self.X,self.Y)
        return clf.coef_
        
    def RidgeRegression(self):
        clf = lm.Ridge(alpha=1.0)
        clf.fit(self.X,self.Y)
        return clf.coef_
        
if __name__=='__main__':
    inputMat = np.array([np.random.randn(100),np.random.randn(100),np.random.randn(100)]).T
    outputMat = np.random.randn(100)
    
    reg = Regressor(inputMat,outputMat)
    lincoeff = reg.linearRegression()
    ridcoeff = reg.RidgeRegression()
    