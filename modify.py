import numpy as np

def modify_histogram(imhist, t_down, t_up):
    L = len(imhist)
    res = np.zeros(L)
    for i in range(0,L):
        if (imhist[i] == 0):
            res[i] = 0
        elif (imhist[i] <= t_down) :
            res[i] = t_down
        elif (imhist[i] < t_up):
            res[i] = imhist[i]
        else:
            res[i] = t_up
    return res