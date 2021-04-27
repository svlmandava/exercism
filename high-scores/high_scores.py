def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    lis = sorted(scores)[::-1]
    return lis[0:3]
