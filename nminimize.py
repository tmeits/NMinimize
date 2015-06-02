import numpy as np
import scipy
import matplotlib
import pandas

match = lambda a, b: [ b.index(x)+1 if x in b else None for x in a ]

def NRFunc(x):
    """"
    In mathematical optimization, the Rastrigin function is a non-convex function used as a performance test problem for optimization algorithms.
    """"
    A=np.array(x)
    return sum(A^2-10.*np.cos(2.*n(pi)*A))+20.
