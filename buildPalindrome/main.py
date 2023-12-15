def solution(st):
    for i in range(len(st)):
        new_st = st + st[:i][::-1]

        if new_st == new_st[::-1]:
            return new_st
