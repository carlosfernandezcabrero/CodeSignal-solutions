# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ


def solution(n):
    ns = str(n)
    middle = int(len(ns) / 2)

    return sum(map(int, ns[:middle])) == sum(map(int, ns[middle:]))


def test_default_answer():
    assert solution(1230) == True
    assert solution(239017) == False
