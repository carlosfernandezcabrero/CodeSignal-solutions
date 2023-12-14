import re


def solution(address):
    return re.match(r".*@([a-z0-9\-]+\.[a-z]+)", address).group(1)
