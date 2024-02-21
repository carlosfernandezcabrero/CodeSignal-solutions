def solution(param1, param2):
    max_len = max(len(str(param1)), len(str(param2)))

    param1 = str(param1).zfill(max_len)
    param2 = str(param2).zfill(max_len)

    return int(
        "".join([str((int(param1[i]) + int(param2[i])) % 10) for i in range(max_len)])
    )
