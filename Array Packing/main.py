def solution(a):
    return int("".join(list(map(lambda x: format(x, "08b"), a))[::-1]), 2)
