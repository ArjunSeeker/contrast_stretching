import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path = "input_images/tree.png"
img = cv.cvtColor(cv.imread(path), cv.COLOR_BGR2GRAY)
# hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * float(hist.max()) / cdf.max()
# plt.plot(cdf_normalized, color='b')
# plt.hist(img.flatten(), 256, [0, 256], color='r')
# plt.xlim([0, 256])
# plt.legend(('cdf', 'histogram'), loc='upper left')
# plt.show()


equ = cv.equalizeHist(img)
cv.imwrite('tree.png', equ)
cv.imshow('equ.png', equ)
cv.waitKey(0)
cv.destroyAllWindows()
hist, bins = np.histogram(equ.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(equ.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()
