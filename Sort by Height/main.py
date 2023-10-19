def solution(a):
    clean_vector = [x for x in a if x != -1]
    clean_vector.sort()

    for i in range(len(a)):
        if a[i] == -1:
            continue

        a[i] = clean_vector[0]
        clean_vector.pop(0)

    return a
