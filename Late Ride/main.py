def solution(n):
    secs = n % 60
    mins = n // 60

    digits = "%d%d" % (mins, secs)

    return sum([int(digit) for digit in digits])
