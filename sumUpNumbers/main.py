import re


def solution(inputString):
    return sum(map(int, re.findall(r"\d+", inputString)))
