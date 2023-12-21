def solution(s):
    c = 0
    o = ""

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            c += 1
        else:
            if c > 0:
                o += str(c + 1) + s[i]
                c = 0
            else:
                o += s[i]

    return o
