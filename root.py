import cv2
import os
import numpy as np
from statistics import mean, pstdev
from numpy.lib.function_base import average
from make_histogram import *
from modify import *
from local_maxima import *
from histogram_equalize import *
from plot_histogram import *


def getRcv(original_hist, modified_hist):
    cv0 = pstdev(original_hist)/mean(original_hist)
    cv1 = pstdev(modified_hist)/mean(modified_hist)
    return cv1/cv0


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

    Rcv_0 = getRcv(histogram, imhist_modified)
    if Rcv_0 < 0.5:
        Rcv_exp = 0.5*0.6 + Rcv_0*0.4
        T_up1 = max(histogram)
        while abs(t_up-T_up1) > 1:
            T_up = 0.5*(t_up + T_up1)
            T_down = Sta/M
            imhist_modified = modify_histogram(histogram, T_down, T_up)
            Rcv = getRcv(histogram, imhist_modified)
            if Rcv < Rcv_exp:
                t_up = T_up
            else:
                T_up1 = T_up

    else:
        T_up = t_up
        T_down = t_down

    mean_h = mean(histogram)
    if T_down > 0.2 * mean_h:
        T_down = 0.2 * mean_h
        imhist_modified = modify_histogram(histogram, T_down, T_up)
    print('modified parameters:')
    print("T_up %d" % T_up)
    print("T_down %d" % T_down)
    res = histogram_equalization(im, interval2, imhist_modified, 0, 255)
    cv2.imwrite("street.jpg", res)
    plot_hist(res, N)


if __name__ == "__main__":
    image = cv2.cvtColor(cv2.imread(
        'input_images/street.bmp'), cv2.COLOR_BGR2GRAY)
    image = np.array(image)
    main(image)
