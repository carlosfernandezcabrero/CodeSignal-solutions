import re


def solution(a):
    return re.match(r"^[a-zA-Z_]\w*$", str(a)) != None
