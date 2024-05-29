def solution(n):

    def get_weakness(n):
        return len([_i for _i in range(1, n + 1) if n % _i == 0])

    max_weakness = 0
    num_max_weakness = 0

    weaknesses = {}
    for i in range(1, n + 1):
        weaknesses[i] = get_weakness(i)

    for i in range(n, 0, -1):
        if i - 1 < max_weakness:
            break

        weakness = weaknesses[i]
        weakness_count = 0

        for k, v in weaknesses.items():
            if k < i and v > weakness:
                weakness_count += 1

        if weakness_count > max_weakness:
            max_weakness = weakness_count
            num_max_weakness = 1
        elif weakness_count == max_weakness:
            num_max_weakness += 1

    return [max_weakness, num_max_weakness]
