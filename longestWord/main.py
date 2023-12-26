import re


def solution(text):
    return sorted(re.findall(r"[a-zA-Z]+", text), key=len, reverse=True)[0]
