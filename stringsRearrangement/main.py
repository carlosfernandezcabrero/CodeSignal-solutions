import itertools


def solution(a):
    def check(permutation):
        for i in range(len(permutation) - 1):
            if (
                sum(
                    [
                        1 if permutation[i][j] != permutation[i + 1][j] else 0
                        for j in range(len(permutation[i]))
                    ]
                )
                != 1
            ):
                return False
        return True

    for i in itertools.permutations(a):
        if check(i):
            return True

    return False
