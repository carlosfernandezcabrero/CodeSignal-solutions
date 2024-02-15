# l ≤ A ≤ B ≤ r


def solution(n, l, r):
    a = l
    b = n - a
    c = 0

    while a <= b and (a + b) == n:
        if l <= a <= b <= r:
            c += 1

        a += 1
        b -= 1

    return c
