# -*- coding: utf-8 -*-
"""
Lists: search algorithms
"""


"""
sequential searches
"""

def find(x, L):
    '''
    returns the position of x in L or -1 if not present
    '''
    (i, n) = (0, len(L))
    while (i < n) and (x != L[i]):
        i += 1
    if i < n:
        return i
    else:
        return -1

def findSorted(x, L):
    '''
    returns the position of x in L sorted or -1 if not present
    '''
    (i, n) = (0, len(L))
    while (i < n) and (x > L[i]):
        i += 1
    if i < n and L[i] == x:
        return i
    else:
        return -1


"""
binarySearch
"""
        
def __binarySearch(x, L, left, right):
    '''
    returns the position of x in L[left, right[ 
    or its expected position if not present
    '''
    if left == right:
        return right
    else:
        mid = left + (right - left) // 2
        if x == L[mid]:
            return mid
        else:
            if x < L[mid]:
                return __binarySearch(x, L, left, mid)
            else:
                return __binarySearch(x, L, mid+1, right)
                
    
def binarySearch(x, L):
    '''
    returns the position of x in L sorted or -1 if not present
    '''
    p = __binarySearch(x, L, 0, len(L))
    if (p < len(L)) and (L[p] == x):
        return p
    else:
        return -1
        

def binarysearch_iter(L, x):
    left = 0
    right = len(L)
    m = left + (right - left) // 2
    while left != right and x != L[m] :
        if x < L[m]:
            right = m
        else:
            left = m + 1
        m = left + (right - left) // 2
    if left == right:
        return -1 # right if we woant the position where x might be
    else:
        return m