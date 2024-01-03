def solution(matrix):
    squares_set = set()

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            square = (
                matrix[i][j],
                matrix[i][j + 1],
                matrix[i + 1][j],
                matrix[i + 1][j + 1],
            )

            squares_set.add(square)

    return len(squares_set)
