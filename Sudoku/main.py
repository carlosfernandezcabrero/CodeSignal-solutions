import numpy as np


def solution(grid):
    array = np.array(grid)
    array_transpose = array.transpose()

    for row in range(0, 9, 3):
        for x in range(3):
            if len(set(array[row + x])) != 9:
                return False

            if len(set(array_transpose[row + x])) != 9:
                return False

        for col in range(0, 9, 3):
            subgrid = np.array(
                [
                    array[row, col : col + 3],
                    array[row + 1, col : col + 3],
                    array[row + 2, col : col + 3],
                ]
            ).flatten()

            if len(set(subgrid)) != 9:
                return False

    return True
