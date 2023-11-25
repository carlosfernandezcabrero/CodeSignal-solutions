import string

chessboard = [
    "01010101",
    "10101010",
    "01010101",
    "10101010",
    "01010101",
    "10101010",
    "01010101",
    "10101010",
]
letters = string.ascii_uppercase[:8]


def solution(a1, a2):
    x1, y1 = [*a1]
    x2, y2 = [*a2]

    y1 = int(y1) - 1
    y2 = int(y2) - 1

    return chessboard[y1][letters.find(x1)] == chessboard[y2][letters.find(x2)]
