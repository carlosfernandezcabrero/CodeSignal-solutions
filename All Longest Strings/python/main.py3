def solution(inputArray):
    max_len = max([len(x) for x in inputArray])
    return [x for x in inputArray if len(x) == max_len]
