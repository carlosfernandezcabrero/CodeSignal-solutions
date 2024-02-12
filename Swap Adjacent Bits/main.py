def solution(n):
    return int(
        "".join(
            "{0:032b}".format(n)[i + 1] + "{0:032b}".format(n)[i]
            for i in range(0, len("{0:032b}".format(n)), 2)
        ),
        2,
    )
