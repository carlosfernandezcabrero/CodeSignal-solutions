ms1 = {"L": 1, "R": -1, "A": -2}
ms2 = {"L": -1, "R": 1, "A": -2}


def solution(commands):
    pos1, pos2 = [], []

    if len(commands) == 0:
        return 0

    pos1.append((ms1[commands[0]]) % 4)
    pos2.append((ms2[commands[0]]) % 4)

    for ci in range(1, len(commands)):
        c = commands[ci]

        pos1.append((pos1[-1] + ms1[c]) % 4)
        pos2.append((pos2[-1] + ms2[c]) % 4)

    return len(list(filter(lambda x: x[0] == x[1], zip(pos1, pos2))))
