def solution(votes, k):
    votes_sorted = sorted(votes, reverse=True)

    if votes_sorted[0] != votes_sorted[1] and k == 0:
        return 1

    max = votes_sorted[0]
    winners = 0

    for i in votes_sorted:
        if i + k > max:
            winners += 1
        else:
            break

    return winners
