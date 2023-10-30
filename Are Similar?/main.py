def solution(a, b):
    if len(a) != len(b):
        return False

    differences = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            differences += 1
            if differences > 2:
                return False

    first_diff_index = None
    for i in range(len(a)):
        if a[i] != b[i]:
            if first_diff_index is None:
                first_diff_index = i
            else:
                aux = a[first_diff_index]
                a[first_diff_index] = a[i]
                a[i] = aux
                break

    return a == b
