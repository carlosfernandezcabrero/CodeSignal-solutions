def solution(n):
    return pow(
        2,
        len(format(n, "b"))
        - (
            len(
                format(n, "b")[
                    0 : format(n, "b")[0 : format(n, "b").rfind("0")].rfind("0")
                ]
            )
            + 1
        ),
    )
