def solution(a):
    b = a.split(".")

    return len(b) == 4 and all(
        i.isdigit() and not (i[0] == "0" and len(i) > 1) and 0 <= int(i) < 256
        for i in b
    )
