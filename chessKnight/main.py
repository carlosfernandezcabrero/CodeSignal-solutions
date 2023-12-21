ms = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
square_limit = 8


def solution(c):
    x, y = ord(c[0]) - 96, int(c[1])

    return sum(
        [1 for m in ms if 0 < x + m[0] <= square_limit and 0 < y + m[1] <= square_limit]
    )
