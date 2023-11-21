from math import floor


def solution(a):
    o = []

    for y in range(0, len(a)):
        if y + 2 >= len(a):
            break

        o.append([])

        for x in range(0, len(a[y])):
            if x + 2 >= len(a[y]):
                break

            o[y].append(floor(sum([sum(a[y + i][x : x + 3]) for i in range(0, 3)]) / 9))

    return o
