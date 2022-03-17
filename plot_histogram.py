import numpy as np
from matplotlib import pyplot as plt


def plot_hist(res, N):
    hist, bins = np.histogram(res.flatten(), N, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(res.flatten(), N, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()
