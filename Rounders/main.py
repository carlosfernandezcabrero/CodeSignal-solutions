def solution(n):
    z = 0

    while n > 10:
        r = n % 10
        n //= 10

        if r >= 5:
            n += 1

        z += 1

    return n * (10**z)
