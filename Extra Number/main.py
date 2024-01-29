from collections import Counter


def solution(a, b, c):
    return Counter([a, b, c]).most_common()[-1][0]
