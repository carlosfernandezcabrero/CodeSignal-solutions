operations = ["+", "-", "*", "/"]


def solution(a, b, c):
    for op in operations:
        if eval(f"{a}{op}{b}") == c:
            return True

    return False
