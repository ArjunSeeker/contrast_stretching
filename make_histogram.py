import numpy as np

def make_histogram(ordered, interval):
    n = len(ordered)
    m = len(interval)
    res = np.zeros(m)
    count = 0;
    for i in range(0,n):
        if (ordered[i] <= interval[count]):
            res[count]+=1
        else :
            while (ordered[i] > interval[count]):
                count+=1; 
                if count>= m: break
            if (count >= m):
                break
            res[count] += 1; 
    return res;
