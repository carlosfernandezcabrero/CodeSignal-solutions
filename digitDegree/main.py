def solution(n):
    c = 0

    while n > 9:
        n = sum(map(int, str(n)))
        c += 1

    return c
