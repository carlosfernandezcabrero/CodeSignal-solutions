def solution(k):
    r = 0
    y = 0

    for i in range(1, k + 1):
        number_to_add = i * i

        if i % 2 == 0:
            r += number_to_add
        else:
            y += number_to_add

    return r - y
