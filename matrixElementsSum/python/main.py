FREE_ROOM = 0


def solution(matrix):
    suitable_rooms = 0
    columns_haunted = set()

    for i in range(len(matrix)):
        for j, val in enumerate(matrix[i]):
            if val == FREE_ROOM:
                columns_haunted.add(j)
                continue
            if j in columns_haunted:
                continue

            suitable_rooms += val

    return suitable_rooms
