from collections import Counter


def solution(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    reduced_string = "".join(set(s1)) + "".join(set(s2))

    counter_reduced_string = Counter(reduced_string).most_common()

    matchs = [i for i in counter_reduced_string if i[1] > 1]

    result = 0
    for match in matchs:
        result += min(s1_counter[match[0]], s2_counter[match[0]])

    return result


print(solution("zzzz", "zzzzzzz"))
