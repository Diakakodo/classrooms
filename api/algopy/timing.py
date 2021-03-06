# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:34:21 2017

to compare execution durations...
"""

import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f.__name__, 'function took',(time2-time1)*1000.0,'ms')
        return ret, (time2-time1)*1000.0
    return wrap