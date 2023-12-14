import string

lowercase = string.ascii_lowercase


def solution(inputString):
    inputString = "".join(sorted(inputString))

    if "".join(sorted(set(inputString))) not in lowercase or inputString[0] != "a":
        return False

    lastCharCount = None
    charsCount = 0

    for i in range(len(inputString)):
        if len(inputString) - 1 == i or inputString[i] != inputString[i + 1]:
            charsCount += 1

            if lastCharCount and lastCharCount < charsCount:
                return False

            lastCharCount = charsCount
            charsCount = 0
            continue

        charsCount += 1

    return True
