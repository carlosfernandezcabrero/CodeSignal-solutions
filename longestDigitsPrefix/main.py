import re


def solution(inputString):
    return re.match(r"^\d*", inputString).group()
