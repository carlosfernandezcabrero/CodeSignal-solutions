def solution(inputArray):
    mds = []

    for i in range(len(inputArray) - 1):
        mds.append(abs(inputArray[i] - inputArray[i + 1]))

    return max(mds)
