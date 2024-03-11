import math


def solution(n, m):
    return n + m + math.gcd(n, m) - 2
