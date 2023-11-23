import string


def solution(a):
    d = string.ascii_lowercase
    return "".join([d[(d.find(i) + 1) % len(d)] for i in a])
