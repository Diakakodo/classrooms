# -*- coding: utf-8 -*-
"""BTree Module.
BTree class definition and standard methods and functions.
*Warning:*  Set ``BTree.degree`` before any tree instanciation.
"""

from . import queue
from .queue import Queue


class BTree:
    """BTree class.
    Attributes:
        degree (int): Degree for all existing trees.
        keys (list[Any]): List of node keys.
        children (list[BTree]): List of children.
    """
    
    degree = None

    def __init__(self, keys=None, children=None):
        """BTree instance constructor.
        Args:
            keys (list[Any]).
            children (list[BTree])
        """
        self.keys = keys if keys else []
        self.children = children if children else []

    @property
    def nbkeys(self):
        """Number of keys in node.
        Returns:
            int.
        """
        return len(self.keys)


# B-tree -> linear rep.
def __tolist(B):
    s = '(<' 
    for i in range(B.nbkeys-1):
        s += str(B.keys[i]) + ','
    s += str(B.keys[B.nbkeys-1]) + '>'
    for child in B.children:
        s += __tolist(child)
    s += ')'
    return s

def tolist(B):
    if B:
        return __tolist(B)
    else:
        return ""
        
        
#to build examples linear rep -> B-tree
def __fromlist(s, i=0): 
    if i < len(s) and s[i] == '(':   #useless if string well-formed
        i = i + 2 # to pass the '(<'
        B = BTree()
        while s[i] != '>':
            key = ""            
            while not(s[i] in ',>'):
                key += s[i]
                i += 1
            B.keys.append(int(key))
            if s[i] == ',':
                i += 1 
        i += 1  # to pass the '>'
        B.children = []
        while s[i] != ')':
            (C, i) = __fromlist(s, i)
            B.children.append(C)
        i = i + 1   # to pass the ')'
        return (B, i)
    else:
        return None

def fromlist(s, d):
    BTree.degree = d
    (B, _) = __fromlist(s)
    return B


def __testnode(B, root = False):
    """Test if B root is a valid k-node with k in [B.degree, 2*B.degree]
    """
    return (B.children == [] or len(B.children) == len(B.keys)+1) \
            and (root or B.degree-1 <= B.nbkeys) and B.nbkeys <= 2*B.degree-1 
            
def __isvalid(ref, inf, sup, root = False):
    """Auxiliary function for isvalid.
    Checks order of keys in BTree node and if all have values in
    between second and third arguments.
    Checks also if leaves are all at same level
    Args:
        ref (BTree).
        inf (int): Lower interval bound for key values.
        sup (int): Upper interval bound for key values.
        root (bool): True if initial root
    Returns:
        bool * int.
    """

    if not __testnode(ref, root): 
        return (False, 0)
    if ref.keys[0] <= inf or ref.keys[ref.nbkeys-1] >= sup:
        return (False, 0)
    else:
        for i in range(ref.nbkeys-1):
            if ref.keys[i] >= ref.keys[i+1]:
                return (False, 0)
        if ref.children:
            (ok, height) = __isvalid(ref.children[0], inf, ref.keys[0])
            if not ok:
                return (False, 0)
            for i in range(1, ref.nbkeys):
                (ok, h) = __isvalid(ref.children[i], ref.keys[i-1], ref.keys[i])
                if not ok or h != height:
                    return (False, 0)
            (ok, h) =  __isvalid(ref.children[-1], ref.keys[-1], sup)
            if not ok or h != height:
                return (False, 0)
            else:
                return (True, height + 1)
                
        else:
            return (True, 0)
    
    
def isvalid(ref):
    """Checks if BTree object is has a valid BTree structure.
    In case of multiple tests, BTree.degree must be verified... 
    Args:
        ref (BTree).
    Returns:
        bool: True if BTree has valid structure False if not.
    """

    return ref is None or __isvalid(ref, -float('inf'), float('inf'), root=True)[0]


# display version 1 : creation of the dot -> use graphviz.Source

def __node_dot(ref):
    """Gets node into dot proper shape.
    Args:
        ref (BTree).
    """

    s = str(id(ref)) + '[label="'
    for i in range(ref.nbkeys-1):
        s += str(ref.keys[i]) + ' | '
    s += str(ref.keys[ref.nbkeys-1])
    s +=  '"];\n'
    return s


def __link_dot(ref_a, ref_b):
    """Writes down link between two BTree nodes in dot format.
    Args:
        ref_A (BTree).
        ref_B (BTree).
    """

    return "   " + str(id(ref_a)) + " -- " + str(id(ref_b)) + ";\n"


def dot(ref):
    """Writes down dot format of tree.
    Args:
        ref (BTree).
    Returns:
        str: String storing dot format of BTree.
    """

    s = "graph " + str(ref.degree) + " {\n"
    s += "node [shape = record, height=.1];\n"
    q = Queue()
    q.enqueue(ref)
    s += __node_dot(ref)
    while not q.isempty():
        ref = q.dequeue()
        for child in ref.children:
            s += __node_dot(child)
            s += __link_dot(ref, child)
            q.enqueue(child)
    s += "}"
    return s

def display(ref, *args, **kwargs):
    """Render a BTree to for in-browser display.
    *Warning:* Made for use within IPython/Jupyter only.
    Extra non-documented arguments are passed to the ``dot`` function and
    complyt with its documentation.
    Args:
        ref (BTree).
    Returns:
        Source: Graphviz wrapper object for BTree rendering.
    """

    # Ensure all modules are available
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot(ref, *args, **kwargs)
    display(Source(dot_source))


# display version 2 : creation of a graphviz.Graph object
    
def displaySVG(ref, filename='temp'):
    """Render a BTree to SVG format.
    *Warning:* Made for use within IPython/Jupyter only.
    Args:
        ref (BTree).
        filename (str): Temporary filename to store SVG output.
    Returns:
        SVG: IPython SVG wrapper object for BTree.
    """

    # Ensure all modules are available
    try:
        from graphviz import Graph, Source
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse Btree and generate temporary Graph object
    output_format = 'svg'
    graph = Graph(filename, format=output_format)
    q = Queue()
    if ref is not None:
        q.enqueue(ref)
    while not q.isempty():
        ref = q.dequeue()

        node_label = ''
        for i in range(ref.nbkeys-1):
            node_label += str(ref.keys[i]) + ' | '
        node_label += str(ref.keys[ref.nbkeys - 1])
        graph.node(str(id(ref)), label=node_label,
                   style="rounded", shape="record")

        for child in ref.children:
            graph.edge(str(id(ref)), str(id(child)))
            q.enqueue(child)
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)
