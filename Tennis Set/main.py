def solution(score1, score2):
    min_score, max_score = sorted([score1, score2])

    return max_score == 6 and min_score < 5 or max_score == 7 and min_score in [5, 6]
