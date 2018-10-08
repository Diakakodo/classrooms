# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:58:22 2016
@author: Nathalie
"""
from random import randint

def buildRandomList(n, maxval):
    '''
    build a list with n random values form 0 to maxval
    '''
    L = []
    for i in range(n):
        L.append(randint(0, maxval))
    return L
    
def buildRandomSortedList(n, step):
    '''
    build a sorted list with n values
    step is the maximum difference between values
    '''
    L = [0]
    for i in range(1, n):
        L.append(L[i-1] + randint(0, step))
    return L
    
    