def solution(a):
    team1 = 0
    team2 = 0

    for idx, value in enumerate(a):
        if idx % 2 == 0:
            team1 += value
        else:
            team2 += value

    return [team1, team2]
