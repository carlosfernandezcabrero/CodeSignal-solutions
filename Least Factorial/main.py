import math


def solution(n):
    m = k = 1

    while k < n:
        m += 1
        k = math.factorial(m)

    return k
