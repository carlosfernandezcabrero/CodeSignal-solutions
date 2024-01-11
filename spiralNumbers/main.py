def solution(n):
    o = [[0 for _ in range(n)] for _ in range(n)]
    gc = 1
    d = 0

    while d <= n // 2:
        for i in range(n - d * 2):
            o[d][i + d] = gc
            gc += 1

        for i in range(n - d * 2 - 1):
            o[i + d + 1][n - d - 1] = gc
            gc += 1

        for i in range(n - d * 2 - 1):
            o[n - d - 1][n - d - i - 2] = gc
            gc += 1

        for i in range(n - 2 - d * 2):
            o[n - d - i - 2][d] = gc
            gc += 1

        d += 1

    return o
