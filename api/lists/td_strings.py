# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:39:18 2015

@author: Nathalie
"""

''' 3 ways to traverse a string or a list '''

def print_string(s):
    i = 0
    n = len(s)
    while i < n:
        print(s[i])
        i = i + 1

def print_string2(s):
    for i in range(len(s)):
        print(s[i], end='-')

def print_string3(s):
    for c in s:
        print(c, end='')

def count(c, s):
    cpt = 0
    for char in s:
        cpt += char == c   # a boolean in arithmetic expression become an int!
    return cpt

def in_string(c, s):
    '''
    tests whether character c is in string s
    '''
    i = 0
    n = len(s)
    while (i < n) and (s[i] != c):
        i = i + 1
    if i < n:
        return i
    else:
        return -1
    
def palindrome(s):
    '''    
    tests whether s is a palindrome
    '''
    i = 0
    n = len(s)
    while (i < n//2) and (s[i] == s[n-i-1]):
        i = i+1
    return (i == n//2)

def palindrome2(s):
    i = 0
    j = len(s)-1
    while (i < j) and (s[i] == s[j]):
        if s[i] == ' ':
            i = i+1
        if s[j] == ' ':
            j = j-1
        i = i+1
        j = j-1
    return (i >= j)
    
    
def substring(s, str):
    '''
    returns the position of s in str, -1 is s not in str
    '''
    n = len(s)
    n2 = len(str)
    i = 0
    while (i <= n2 - n):
        j = 0
        while (j < n) and (s[j] == str[i+j]):
            j = j + 1
        if j == n:
            return i
        i = i + 1
    return -1

# same without return in loop
def substring2(s, str):
    '''
    returns the position of s in str, -1 is s not in str
    '''
    n = len(s)
    n2 = len(str)
    i = 0
    ok = False
    while (i <= n2 - n) and not ok:  # ok peut être remplacé par j == n
        j = 0
        while (j < n) and (s[j] == str[i+j]):
            j = j + 1
        ok = j == n
        i = i + 1
    if ok:
        return i-1
    else:
        return -1
