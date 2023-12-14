import string

x = string.ascii_lowercase


def solution(bishop, pawn):
    x1 = x.index(bishop[0])
    y1 = int(bishop[1]) - 1

    x2 = x.index(pawn[0])
    y2 = int(pawn[1]) - 1

    return abs(x1 - x2) == abs(y1 - y2)
