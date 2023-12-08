def solution(upSpeed, downSpeed, desiredHeight):
    f = upSpeed - downSpeed

    if desiredHeight <= upSpeed or desiredHeight <= f:
        return 1

    if f == 1:
        return desiredHeight - upSpeed + 1

    d = 2
    ac = upSpeed + f

    while True:
        if ac >= desiredHeight:
            return d

        ac += f
        d += 1
