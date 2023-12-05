def solution(inputArray, k):
    draft = inputArray.copy()

    for i in range(len(inputArray)):
        if (i + 1) % k == 0:
            draft.remove(inputArray[i])

    return draft
