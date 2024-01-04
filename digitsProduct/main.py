def solution(p):
    if p == 0:
        return 10
    if p < 10:
        return p

    o = []

    for i in range(9, 1, -1):
        while p > 1 and p % i == 0:
            o.insert(0, str(i))
            p //= i

    if p != 1:
        return -1

    return int("".join(o))
