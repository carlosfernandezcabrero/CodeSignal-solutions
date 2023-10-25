import re


def solution(inputString):
    while True:
        matches = set(re.findall(r"\((\w*)\)", inputString))

        if not matches:
            break

        for match in matches:
            reversed_string = match[::-1]
            inputString = inputString.replace(f"({match})", reversed_string)

    return inputString
