import numpy as np

def histogram_equalization(im, interval2, imhist_modified, min_range, max_range):
    [nrow, ncol] = np.shape(im)
    L = len(imhist_modified)

    res = np.zeros((nrow,ncol))
    
    cumulative = np.zeros(L)
    cumulative[0] = 0;

    for i in range(1,L):
        cumulative[i] = cumulative[i-1] + imhist_modified[i];
    fm = cumulative[L-1] if cumulative[L-1] != 0 else 1

    hist_equalized = np.zeros(L)

    for i in range(0,L):
        hist_equalized[i] = (max_range - min_range) * cumulative[i] / fm + min_range;
    for i in range(0,nrow):
        for j in range(0,ncol):
            tmp_k = 0;
            tmp_k_ratio = 0;
            
            for l in range(0,L):
                if (im[i][j] <= interval2[l]):
                    tmp_k = l;
                    tmp_min_range = interval2[l-1] if l>0 else 0

                    if (interval2[l] - tmp_min_range != 0):
                        tmp_k_ratio = (im[i][j] - tmp_min_range) / (interval2[l] - tmp_min_range);
                    else:
                        tmp_k_ratio = -1;
                    break;

            tmp_min = hist_equalized[tmp_k-1] if tmp_k > 0 else 0
            
            if (tmp_k_ratio >= 0):
                res[i][j] = tmp_k_ratio * (hist_equalized[tmp_k] - tmp_min) + tmp_min
            else:
                res[i][j] = hist_equalized[tmp_k]
    return res;
