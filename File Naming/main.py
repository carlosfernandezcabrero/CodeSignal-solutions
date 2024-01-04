def solution(n):
    for k, v in enumerate(n):
        draft = n[:k]

        if v in draft:
            r = 1
            fn = f"{v}({r})"

            while fn in draft:
                r += 1
                fn = f"{v}({r})"

            n[k] = fn

    return n
