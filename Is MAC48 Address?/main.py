import re


def solution(inputString):
    return re.match(r"^([0-9A-F]{2}-){5}([0-9A-F]{2})$", inputString) != None
