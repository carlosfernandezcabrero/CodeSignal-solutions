def solution(a):
    f = 1
    pf = f
    lp = max(a) + 1

    while True:
        for i in range(0, lp, f):
            if i in a:
                f += 1
                break

        if pf == f:
            break
        else:
            pf = f

    return f
