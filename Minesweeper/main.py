def solution(a):
    o = []
    v_l = len(a) - 1
    cells_to_inspect = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
    ]

    for i in range(len(a)):
        o += [[]]
        h_l = len(a[i]) - 1

        for j in range(len(a[i])):
            b = 0

            for cell_to_inspect in cells_to_inspect:
                x = j + cell_to_inspect[0]
                y = i + cell_to_inspect[1]

                if x >= 0 and x <= h_l and y >= 0 and y <= v_l and a[y][x]:
                    b += 1

            o[i].append(b)

    return o
