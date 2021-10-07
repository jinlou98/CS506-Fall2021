from math import sqrt
# import numpy as np

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    # num of observations in both sets
    both = len(list(set(x).intersection(y)))
    # num of observations in either set
    either = (len(x) + len(y)) - both
    return float(both) / either

def cosine_sim(x, y):
    # a1=np.array(x)
    # a2=np.array(y)
    # sim_scores = a1.dot(a2)/ (np.linalg.norm(a1, axis=1) * np.linalg.norm(a2))
    # return sim_scores
    raise NotImplementedError()

# Feel free to add more
