def solution(value1, weight1, value2, weight2, maxW):
    m = {value1: weight1, value2: weight2}
    o = 0
    c = 0

    for value in sorted(m.keys(), reverse=True):
        weight = m[value]

        if c + weight > maxW:
            continue

        o += value
        c += weight

    return o
