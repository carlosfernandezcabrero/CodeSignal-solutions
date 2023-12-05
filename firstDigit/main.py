import re


def solution(a):
    return re.match(r"[^\d]*(\d)", a).group(1)
