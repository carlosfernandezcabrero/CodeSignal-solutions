def solution(c):
    word = ""

    for i in range(0, len(c), 8):
        word += chr(int(c[i : i + 8], 2))

    return word
