import cv2
import os
import numpy as np
from statistics import mean, pstdev
from numpy.lib.function_base import average
from make_histogram import *
from modify import *
from local_maxima import *
from histogram_equalize import *
from plot_histogram import*


def main(image):
    maxval = image.max()
    minval = image.min()
    print('max pixel', maxval)
    print('min pixel', minval)
    N = 500
    step = (maxval-minval)/(N+1)
    print('interval', step)
    interval = list(np.arange(minval, maxval, step))
    interval1 = interval[1:(len(interval)-1)]
    interval2 = interval[2:len(interval)]
    im = np.array(image)
    ordered = im.flatten()
    ordered.sort()
    histogram = make_histogram(ordered, interval2)
    idx_imhist_not0 = histogram != 0
    imhist_not0 = histogram[idx_imhist_not0]
    local_maximums = find_local_maximum(imhist_not0, 10)
    t_up = average(local_maximums)
    print('tup', t_up)
    dim_im = np.shape(im)
    print('shape', dim_im)

    d_min = (255) / N  # minimum gray level interval in modified histogram
    n_total = dim_im[0] * dim_im[1]
    L = len(histogram)
    Sta = min(n_total, t_up * L)
    M = N
    t_down = d_min * Sta / M
    print("T_Down", t_down)

    if t_down > t_up:
        t_up, t_down = t_down, t_up
        print("the values have been swapped")
    imhist_modified = modify_histogram(histogram, t_down, t_up)
    res = histogram_equalization(im, interval2, imhist_modified, 0, 255)
    cv2.imwrite("street.png", res)

    # plotting the histogram of the image obtained after ADPHE
    plot_hist(res, N)


if __name__ == "__main__":
    image = cv2.cvtColor(cv2.imread(
        'input_images/street.bmp'), cv2.COLOR_BGR2GRAY)
    image = np.array(image)
    main(image)
