# -*- coding: utf-8 -*-
"""
from Architecture lecture!
Conversion decimal <-> two's complement representation 
@author: Nathalie
"""

# simple conversions

def dec_to_bin(n, p):
    '''
    transform a decimal in binary (as a string) with p bits
    '''
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    while len(s) < p:   # add the missing '0'
        s = '0' + s
    return s
    
    
def bin_to_dec(s):
    '''
    transform a binary (string) in decimal
    '''
    n = 0
    for b in s:
        n = n * 2 + int(b)
    return n

# decimal <-> two's complement

def integer_to_twoscomp(n, p):
    '''
    returns the p-bits two's complement representation 
    of the integer n
    '''
    if n < 0:
        n = 2**p + n
    return dec_to_bin(n, p)

def not_b(c):
    if c == '1':
        return '0'
    else:
        return '1'

def integer_to_twoscomp2(n, p):
    if n < 0:
        sign = -1
    else:
        sign = 1
    s = dec_to_bin(sign*n, p)
    if sign == -1:
        s2 = ""     # str unmutable
        i = p-1
        while s[i] != '1':      # True eventually
            s2 = s[i] + s2
            i = i - 1
        i = i - 1
        while i >= 0:
            s2 = not_b(s[i]) + s2
            i = i - 1
        s = s2
    return s
    
    
def twoscomp_to_integer(b, p):
    '''
    returns the integer n from its p-bits two's complement representation 
    '''
    n = bin_to_dec(b)    
    if b[0] == '1':
        n = n - 2**p
    return n

def test(n, p):
    return twoscomp_to_integer(integer_to_twoscomp(n,p), p) == n