from collections import Counter


def solution(inputString):
    return len(list(filter(lambda x: x % 2 != 0, Counter(inputString).values()))) <= 1
