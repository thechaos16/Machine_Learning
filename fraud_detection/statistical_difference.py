# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:28:32 2016

@author: minkyu
"""

import numpy as np
from scipy import stats
from scipy.stats import distributions
from collections import namedtuple

def manwhitney_test(bins1, counts1, bins2, counts2):
    if len(bins1) == 1 and len(bins2) == 1:
        return bins1[0] != bins2[0]

    # get sorting indices from pooled keys 1 and 2.
    idx = np.argsort(bins1+bins2)
    # compute ranks from a pool using midrank for the repeating values.
    tie_corrleation = 0
    cur_start_rank = 1
    sum_1 = 0
    sum_2 = 0
    for i in range(len(idx)):
        if idx[i] < len(bins1):
            cur_counts = counts1
            idx_in_hist = idx[i]
        else:
            cur_counts = counts2
            idx_in_hist = idx[i] - len(bins1)

        current_count = cur_counts[idx_in_hist]
        if current_count == 0:
            continue

        cur_rank = current_count * (2 * cur_start_rank + current_count - 1) / 2
        # ... and average to get a midrank. This line can be removed with adjustment
        cur_rank /= current_count
        # of the code below, but it would be better to keep it for readability.
        cur_start_rank += current_count
        if idx[i] < len(bins1):
            sum_1 += cur_rank * current_count
        else:
            sum_2 += cur_rank * current_count

        if current_count > 1:
            tie_corrleation += current_count * current_count * current_count - current_count
            
    size1 = np.sum(counts1)
    size2 = np.sum(counts2)
    size_total = (size1 + size2)
    tie_corrleation /= size_total * (size_total - 1)
    u_1 = sum_1 - size1 * (size1 + 1) / 2
    u_2 = sum_2 - size2 * (size2 + 1) / 2
    
    # validity check
    if size1 * size2 != u_1 + u_2:
        pass
        # raise ValueError

    # compute p-value for the two-sided test
    sd = np.sqrt(size1 * size2 * (size_total + 1 - tie_corrleation) / 12.0)
    mean = (u_1 + u_2) / 2
    z = np.abs(u_1 - mean) / sd
    p_value = (distributions.norm.sf(z) * 2)
    result = namedtuple('stat_result', ['p_val', 'score'])
    return result(p_value, z)

def compare_continuous_distribution(data1, data2):
    normal1 = normality_checker(data1)
    normal2 = normality_checker(data2)
    thr = 0.05
    
    # if at least one of distribution is not normal
    if normal1 > thr and normal2 > thr:
        result = stats.ttest_ind(data1, data2)
    else:
        result = stats.ks_2samp(data1, data2)
    return result.pvalue
    
def normality_checker(data):
    result = stats.kstest(data, 'norm')
    return result.pvalue