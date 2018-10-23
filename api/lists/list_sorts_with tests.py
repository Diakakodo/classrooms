# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:15:58 2016
@author: Nathalie & Marwan
"""

from algopy import listtools
from algopy import timing


    
"""
Selection sort
"""


def minimum(L, d, f):
    pos = d
    for i in range(d+1, f+1):
        if L[i] < L[pos]:
            pos = i
    return pos

def minimum2(L, d, f):
    while (d < f):
        if L[d] < L[f]:
            f = f-1
        else:
            d = d+1
    return d
    
@timing.timing
def selectSort(L):
    n = len(L)
    for i in range(n):
        pos = minimum(L, i, n-1)
        (L[i], L[pos]) = (L[pos], L[i]) 
        
'''
In one function, minimum inlined
'''

def selectSort2(l):
    n = len(l)
    for i in range(n - 1):
        mp = i
        for j in range(i + 1, n):
            if l[j] < l[mp]:
                mp = j
        l[i], l[mp] = l[mp], l[i]

"""
Insertion sort
"""

def insert(x, L):
    n = len(L)
    # search position
    i = 0
    while (i < n) and (x > L[i]):
        i += 1
    # shifts
    L.append(None)
    for j in range(n, i, -1):
        L[j] = L[j-1]
    # insertion
    L[i] = x

def insert2(x, L):
    '''
    search for place 
    and shifts at the same time
    '''
    i = len(L) - 1
    L.append(None)
    while (i >= 0) and (x < L[i]):
        L[i+1] = L[i]
        i -= 1
    L[i+1] = x

@timing.timing    
def insertSort(L):
    R = []
    for x in L:
        insert2(x, R)
    return R
    
'''
In place : insert2 inlined
'''

def insertSort2(l):
    for i in range(len(l)):
        x = l[i]
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = x


def insert3(x, L, n):
    # search position
    i = 0
    while (i < n) and (x > L[i]):
        i += 1
    # shifts
    for j in range(n, i, -1):
        L[j] = L[j-1]
    # insertion
    L[i] = x

@timing.timing
def insertSort3(L):
    for i in range(1, len(L)):
        insert3(L[i], L, i)
    return L

"""
Bubble sort
"""
@timing.timing
def bubbleSort(L):
    swap = True
    n = len(L)
    while swap:
        swap = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                (L[i], L[i+1]) = (L[i+1], L[i])
                swap = True
        n -= 1
        
"""
Merge sort
"""

def partition(L):
    n = len(L)
    L1 = []
    for i in range(0, n//2):
        L1.append(L[i])
    L2 = []      
    for i in range(n//2, n):
        L2.append(L[i])
    return (L1, L2)


def merge(L1, L2):
    R = []
    i = j = 0
    n1 = len(L1)
    n2 = len(L2)
    while (i < n1) and (j < n2):
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i = i+1
        else:
            R.append(L2[j])
            j = j+1
    for i in range(i, n1):
        R.append(L1[i])
    for j in range(j, n2):
        R.append(L2[j])
    return R

def merge2(L1, L2):
    R = []
    n1 = len(L1)
    n2 = len(L2)
    (i1, i2) = (0, 0)
    for i in range(n1 + n2):
        if (i2 == n2) or (i1 < n1 and L1[i1] <= L2[i2]):
            R.append(L1[i1])
            i1 += 1
        else:
            R.append(L2[i2])
            i2 += 1         
    return R
    

def mergesort(L):
    if len(L) <= 1:
        return L
    else:
        (L1, L2) = partition(L)
        return merge(mergesort(L1), mergesort(L2))

@timing.timing
def callMergeSort(L):
    '''
    just for the timing stuff
    '''
    return mergesort(L)    





"""
Bonus: Quick sort
"""

def partition_p(l, left, right):
    '''
    move all values smaller than mid point in the left part 
    and higher value in the right part
    '''
    pivot = left + (right - left) // 2
    pval = l[pivot]
    l[pivot], l[right - 1] = l[right - 1], l[pivot]
    pivot = left
    for i in range(left, right - 1):
        if l[i] <= pval:
            l[pivot], l[i] = l[i], l[pivot]
            pivot += 1
    l[pivot], l[right - 1] = l[right - 1], l[pivot]
    return pivot

def qsort(l, left, right):
    if right - left > 1:
        pivot = partition_p(l, left, right)
        qsort(l, left, pivot)
        qsort(l, pivot + 1, right)

@timing.timing
def quickSort(l):
    qsort(l, 0, len(l))
        
  

"""
tests
"""
def average(L):
    s = 0
    for x in L:
        s += x
    return(s/len(L))
    
def sortTest(n, essays=1, sorted=False):
    Lselect = []
    Linsert = []
    Lbubble = []
    Lmerge = []
    Lquick = []        
    for i in range(essays):
        if sorted:
            L = listtools.buildRandomSortedList(n, 3)
        else:
            L = listtools.buildRandomList(n, n*10)  
        L2 = list.copy(L)    #deep copy
        Lselect.append(selectSort(L2)[1])
        Linsert.append(insertSort(L)[1])
        L2 = list.copy(L) 
        Lbubble.append(bubbleSort(L2)[1])
        Lmerge.append(callMergeSort(L)[1])
        Lquick.append(quickSort(L)[1])
    d = {}
    d["select"] = average(Lselect)
    d["insert"] = average(Linsert)
    d["bubble"] = average(Lbubble)
    d["merge"] = average(Lmerge)
    d["quick"] = average(Lquick)
    return d

"""
test results:
-----------------------------------------------
>>> sortTest(5000)
selectSort function tooks 1219.6180820465088 ms
insertSort function tooks 1238.8770580291748 ms
bubbleSort function tooks 2505.1989555358887 ms
callMergeSort function tooks 33.02407264709473 ms
quickSort function tooks 15.511035919189453 ms
-----------------------------------------------
>>> sortTest(10000)
selectSort function tooks 4858.057022094727 ms
insertSort function tooks 4947.42488861084 ms
bubbleSort function tooks 9888.34285736084 ms
callMergeSort function tooks 69.5488452911377 ms
quickSort function tooks 30.52210807800293 ms

>>> sortTest(10000, True)
selectSort function tooks 21345.594882965088 ms
insertSort function tooks 15.007972717285156 ms
bubbleSort function tooks 5.000114440917969 ms
callMergeSort function tooks 230.46088218688965 ms
quickSort function tooks 109.98821258544922 ms

n = 5000
{'bubble': 9328.880941867828,
 'insert': 4865.828990936279,
 'merge': 159.39319133758545,
 'quick': 75.61057806015015,
 'select': 4995.196580886841}
 
 n = 5000 sorted
 {'bubble': 3.2257437705993652,
 'insert': 9.92499589920044,
 'merge': 125.70154666900635,
 'quick': 59.36561822891235,
 'select': 4863.577342033386}
{'bubble': 0.8505702018737793,
 'insert': 3.144347667694092,
 'merge': 37.139999866485596,
 'quick': 15.139389038085938,
 'select': 1507.10871219635}
 
 n = 10000
 {'bubble': 18142.90747642517,
 'insert': 9354.629719257355,
 'merge': 118.3908462524414,
 'quick': 54.56579923629761,
 'select': 8790.960323810577}
"""
