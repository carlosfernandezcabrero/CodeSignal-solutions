def solution(inputArray):
    changes = 0

    for i in range(len(inputArray) - 1):
        step = (inputArray[i] - inputArray[i + 1]) + 1

        if step > 0:
            changes += step
            inputArray[i + 1] += step

    return changes
