import numpy as np


def solution(ia, k):
    isum = np.sum(ia[0:k])
    ms = isum

    for i in np.arange(len(ia) - k):
        isum += ia[i + k] - ia[i]
        ms = max(ms, isum)

    return ms
