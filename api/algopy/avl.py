# -*- coding: utf-8 -*-

""" AVL Module

Defines AVL tree class and related functions.
"""

from .queue import Queue
from . import bintree

class AVL:
    """AVL main class."""
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal


#
#def __nodetodot(ref, bal=True):
#    s = str(ref.key) + '[shape="circle"]'   
#    if bal:
#        s += '[xlabel="' + str(ref.bal) + '"]'
#    return s + '\n'
#    
#    
#def dot_simple(ref, bal=True):
#    """Writes down dot format of AVL.
#
#    This is a simple implementation for quick demo and understanding.
#
#    Args:
#        ref (AVL): all keys unique
#
#    Returns:
#        str: String storing dot format of BinTree.
#
#    """
#
#    s = "graph {\n" + 'graph [ordering="out"]\n'
#    q = Queue()
#    if ref:
#        q.enqueue(ref)
#    while not q.isempty():
#        node = q.dequeue()
#        s += __nodetodot(node, bal)
#        if node.left:
#            s += "   " + str(node.key) + " -- " + str(node.left.key) + "\n"
#            q.enqueue(node.left)
#        if node.right:
#            s += "   " + str(node.key) + " -- " + str(node.right.key) + "\n"
#            q.enqueue(node.right)
#    s += "}"
#    return s
#


def __nodeToDot(T, bal=True):
    s = str(id(T)) 
    if T.key != None:
        if bal:
            s += '[label="' + str(T.key) + '", xlabel="' + str(T.bal) + '"]'
        else:
            s += '[label="' + str(T.key) + '"]'
    else:
        s += '[label=""];'
    s += '\n'
    return s
    
def __linkToDot(A, B):
    return "   " + str(id(A)) + " -- " + str(id(B)) + ";\n"

def __nulChild(T, side):
    s = str(id(T)*side) + '[shape=point, color=white]\n'
    return s + "   " + str(id(T)) + " -- " + str(id(T)*side) + "[color=white];\n"

def __toDot(T, all = True):
    s = ""
    if T.left != T.right or all:
        if T.left:
            s += __nodeToDot(T.left)
            s += __linkToDot(T, T.left)
            s += __toDot(T.left)
        else:
            s += __nulChild(T, 2)
        if T.right:
            s += __nodeToDot(T.right)
            s += __linkToDot(T, T.right)
            s += __toDot(T.right)
        else:
            s += __nulChild(T, 3)
    return s

def dot_nath(T):
    if T:
        s = "graph {\n"
        s += "node [shape = circle, width=.5];\n"
        s += __nodeToDot(T)
        return s + __toDot(T) + '}'

def __nodebalance_dict(B, nodes):
    if B is not None:
        nodes[id(B)] = B.bal
        __nodebalance_dict(B.left, nodes)
        __nodebalance_dict(B.right, nodes)        

def __addbalance(dot, nodebal):
    L = dot.splitlines()
    res = ""
    for i in range(len(L)):
        if "[label" in L[i]:
            nodeid = int(L[i][9:18])
            L[i] = L[i][:19] + 'xlabel="' + str(nodebal[nodeid]) + '";' + L[i][19:] 
        res += L[i] + '\n'
    return res        
    
def dot(T, bal = True):
    dotstr = bintree.dot(T)
    if bal:
        nodebal = {}
        __nodebalance_dict(T, nodebal)
        dotstr = __addbalance(dotstr, nodebal)
    return dotstr    

        
def display(ref, *args, **kwargs):
    """Render a BinTree to for in-browser display.

    *Warning:* Made for use within IPython/Jupyter only.

    Extra non-documented arguments are passed to the ``dot`` function and
    complyt with its documentation.

    Args:
        ref (BinTree).

    Returns:
        Source: Graphviz wrapper object for BinTree rendering.

    """

    # Ensure all modules are available
    try:
        from graphviz import Source
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot(ref, *args, **kwargs)
    return Source(dot_source)
