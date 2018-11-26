# -*- coding: utf-8 -*-
"""
February 2018
Binary trees: occurrences and hierarchical numbering
API
"""

from algopy import bintree
from algopy import queue

#------------------------------------------------------------------------------
# 4.2                           Occurrence list display

# with BFS (parcours largeur)

def treeToOccList(B):
    '''
    Builds the list of node occurrences
    '''
    #FIXME
    pass      

# example for codeTree (see below)
L = ['', '0', '1', '10', '11', '100', '101', '110', '111', '1100', '1101']

def printOccList(B):
    '''
    Prints the occurrence list representation of B
    '''
    if B != None:
        L = treeToOccList(B)
        s = '{' + chr(949)  # 'ε'
        for i in range(1, len(L)):
            s += ", " + L[i]
        s += '}'
    print(s)            

         
    

#------------------------------------------------------------------------------
# 4.2                         Prefix code

# tree from 4.2 q 3
from algopy.bintree import BinTree        
codeTree = BinTree(None,
                   BinTree('a',None,None),
                   BinTree(None,
                          BinTree(None,BinTree('c',None,None),BinTree('b',None,None)),
                          BinTree(None,
                                 BinTree(None,BinTree('f',None,None),BinTree('e',None,None)),
                                 BinTree('d',None,None))))

occ = "{ε, 0, 1, 10, 11, 100, 101, 110, 111, 1100, 1101}"


#  q 4
    
def findCode(T, letter, code=''):
    '''
    Find the code of letter
    B is not None 
    B is full (localement complet)
    '''
    #FIXME
    pass
        
            


"""
Hierarchical numbering
"""
#------------------------------------------------------------------------------
             
''' 
Trees as vector (list here) : 
using the hierarchical numbering
T[i] is the value at node number i (T[0] unused...)
'''


#------------------------------------------------------------------------------
#                             Examples

from algopy.bintree import BinTree
B = BinTree(22, 
            BinTree(5, 
                    BinTree(3, BinTree(1, None, None), BinTree(4, None, None)), 
                    BinTree(12, None, BinTree(17, None, None))), 
            BinTree(29, BinTree(23, None, None), None))

# the "hierarchical" representation of tree B:
L = [None, 22, 5, 29, 3, 12, 23, None, 1, 4, None, 17, None, None, None, None, None, None, None, None, None, None, None, None]

# another example:

T_hier = [None]*30
for i in range(1, 9):
    T_hier[i] = i
(T_hier[11], T_hier[14], T_hier[29]) = (11, 14, 29)




    

#------------------------------------------------------------------------------
#  5.3                 Classics written with hierarchical representation

def size_h(T, i = 1):
    if (i >= len(T)) or (T[i] == None):
        return 0
    else:
        return 1 + size_h(T, 2*i) + size_h(T, 2*i+1)
        
def dfs_pref_h(T, i = 1):
    if (i < len(T)) and (T[i] != None):
        print(T[i], end=' ')
        dfs_pref_h(T, 2*i)
        dfs_pref_h(T, 2*i+1)

def bfs_h(T):
    if len(T) > 1 and T[1] != None:
        l = len(T)
        q = queue.Queue()
        q.enqueue(1)
        while not q.isempty():
            no = q.dequeue()
            print(T[no])
            if no < l and T[no] != None:   # left child
                q.enqueue(2 * no)
            if no < l and T[no] != None:   # right child
                q.enqueue(2 * no + 1)

    
#------------------------------------------------------------------------------           
#  5.2                     object implementation <-> hierarchical (list)
     
# from BinTree to hierarchical representation

# version1: the height is given

def __hierFromTree2(B, T, i = 1):
    #FIXME
    pass

def hierFromTree2(B, h):
    T = [None] * (2 ** (h+1))  
    __hierFromTree2(B, T)
    return T
    

    
# q2: list -> object
# from hierarchical representation to BinTree

def hier2tree(L, i = 1):
    #FIXME
    pass
    

