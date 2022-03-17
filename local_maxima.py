import numpy as np


def find_local_maximum(image_hist, n):
    size = len(image_hist)
    nhalf = n // 2
    tmp = np.zeros(size)
    count = 0
    window = []
    max_elem = [0, np.double(0.0)]

    for i in range(0, nhalf+1):
        if (i < size):
            tmp_pair = [i, image_hist[i]]
            window.append(tmp_pair)
            if (image_hist[i] > max_elem[1]):
                max_elem[0] = i
                max_elem[1] = image_hist[i]
    if (max_elem[0] == nhalf):
        tmp[nhalf] = True
        count += 1
    sizeminhalf = size - nhalf

    for i in range(nhalf+1, sizeminhalf):
        max_range = i + nhalf
        window.pop(0)

        tmp_pair = [max_range, image_hist[max_range]]

        window.append(tmp_pair)

        if (image_hist[max_range] > max_elem[1]):
            max_elem[0] = max_range
            max_elem[1] = image_hist[max_range]

        if (max_elem[0] < i - nhalf):
            max_elem[0] = window[0][0]
            max_elem[1] = window[0][1]

            for first, second in window:
                if (second > max_elem[1]):
                    max_elem[0] = first
                    max_elem[1] = second
        if (max_elem[0] == i):
            tmp[i] = True
            count += 1
    res = np.zeros(count)
    if (count > 0):
        tmp_count = 0
        for i in range(0, size):
            if (tmp[i]):
                res[tmp_count] = image_hist[i]
                tmp_count += 1
    return res
