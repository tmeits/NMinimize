import pylab
import numpy as np

match = lambda a, b: [ b.index(x)+1 if x in b else None for x in a ]

def NRFunc(x):
    """
    In mathematical optimization, the Rastrigin function is a non-convex function used as a performance test problem for optimization algorithms.
    http://www.cs.unm.edu/~neal.holts/dga/benchmarkFunction/images/rastriginLatex.png
    """
    A=np.array(x)
    return 10.*len(A) + sum(A^2-10.*np.cos(2.*n(pi)*A))

def initializePopulation(NP, lower, upper):
    """
    Initialize population and some arrays
    """
    lenLower = len(lower)
    popLower = np.tile(np.array(lower), NP).reshape(NP, lenLower)
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html
    popRunif = np.random.uniform(low=0.0, high=1.0, size=NP*lenLower).reshape(NP, lenLower)
    popUpper = np.tile(np.array(upper) - np.array(lower), NP).reshape(NP,lenLower)
    pop = popLower + popRunif * popUpper
    return pop

