def solution(n):
    return max([int(str(n)[:i] + str(n)[i + 1 :]) for i in range(len(str(n)))])
