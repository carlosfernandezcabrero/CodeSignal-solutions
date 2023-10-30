def solution(picture):
    return (
        ["*" * (len(picture[0]) + 2)]
        + ["*" + i + "*" for i in picture]
        + ["*" * (len(picture[0]) + 2)]
    )
