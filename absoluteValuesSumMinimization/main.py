import sys


def solution(a):
    mv = sys.maxsize
    r = None

    for i in a:
        s = 0

        for j in a:
            s += abs(j - i)

        if s < mv:
            mv = s
            r = i

    return r
