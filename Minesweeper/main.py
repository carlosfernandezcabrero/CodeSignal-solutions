def solution(a):
    o = []
    v_l = len(a) - 1

    for i in range(len(a)):
        o += [[]]
        h_l = len(a[i]) - 1

        for j in range(len(a[i])):
            b = 0

            if j > 0 and a[i][j - 1]:
                b += 1
            if j < h_l and a[i][j + 1]:
                b += 1
            if i > 0 and a[i - 1][j]:
                b += 1
            if i < v_l and a[i + 1][j]:
                b += 1
            if i > 0 and j > 0 and a[i - 1][j - 1]:
                b += 1
            if i < v_l and j > 0 and a[i + 1][j - 1]:
                b += 1
            if i > 0 and j < h_l and a[i - 1][j + 1]:
                b += 1
            if i < v_l and j < h_l and a[i + 1][j + 1]:
                b += 1

            o[i].append(b)

    return o
