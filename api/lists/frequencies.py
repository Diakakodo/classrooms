# -*- coding: utf-8 -*-
"""
Created on Oct. 2018
@author: nathalie
"""

from algopy import timing



@timing.timing
def frequent(s):
    '''
    returns (nb, c):
    c: the most frequent char in s
    nb: number of c in s
    '''
    max = 0
    for i in range(len(s)):
        cpt = 0
        for j in range(i, len(s)):
            cpt = cpt + (s[i] == s[j])
        if cpt > max:
            (max, c) = (cpt, s[i])
    return (max, c)
    # this version is in n**2 (n(n+1)/2)

@timing.timing
def frequent2(s):
    max = 0
    for i in range(255):
        cpt = 0
        for ch in s:
            cpt = cpt + (ord(ch) == i)
        if cpt > max:
            (max, c) = (cpt, chr(i))
    return (max, c)
    
def hist(s):
    '''
    returns the histogram of characters in s
    I.e., returns a list (an array) of length 256 giving the number
    of occurrences of each character.
    '''
    h = [0]*256
    for c in s:
        h[ord(c)] += 1
    return h

@timing.timing
def frequent3(s):
    h = hist(s)
    m = 0
    for i in range(1, 255):
        if h[i] > h[m]:
            m = i
    return(h[m], chr(m))

def test(s):
    frequent(s)
    frequent2(s)
    frequent3(s)

'''
to build a string randomly
'''
import random

random.seed()

def buildAleaStr(n):
    s = ""
    for i in range(n):
        s = s + chr(random.randint(0,255))
    return s

'''
result with a string of 50000 characters :
>>> test(s)
frequent function took 229260.82491874695 ms
frequent2 function took 1552.1481037139893 ms
frequent3 function took 15.62809944152832 ms
'''




