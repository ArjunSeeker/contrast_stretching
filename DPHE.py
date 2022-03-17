import cv2
import os
import numpy as np
from statistics import mean, pstdev
from numpy.lib.function_base import average
from make_histogram import *
from modify import *
from local_maxima import *
from histogram_equalize import *
from matplotlib import pyplot as plt


def main(image):
    maxval = image.max()
    minval = image.min()
    print('max pixel', maxval)
    print('min pixel', minval)
    N = 500
    step = (maxval-minval)/(N+1)
    print('interval', step)
    interval = list(np.arange(minval, maxval, step))
    interval2 = interval[2:len(interval)]
    im = np.array(image)
    ordered = im.flatten()
    ordered.sort()
    histogram = make_histogram(ordered, interval2)
    dim_im = np.shape(im)
    print('shape', dim_im)
    n_total = dim_im[0] * dim_im[1]
    t_up = 0.25 * n_total
    t_down = 0.075 * n_total
    print('t_up', t_up)
    print('t_down', t_down)

    imhist_modified = modify_histogram(histogram, t_down, t_up)
    res = histogram_equalization(im, interval2, imhist_modified, 0, 255)
    cv2.imwrite("tree.png", res)

    hist, bins = np.histogram(res.flatten(), N, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(res.flatten(), N, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


if __name__ == "__main__":
    image = cv2.cvtColor(cv2.imread(
        'input_images/tree.png'), cv2.COLOR_BGR2GRAY)
    image = np.array(image)
    main(image)
