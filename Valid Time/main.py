from datetime import datetime


def solution(time):
    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        return False

    return True
