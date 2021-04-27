def latest(scores):
    rev = scores[::-1]
    return rev[0]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    lis = sorted(scores)[::-1]
    return lis[0:3]
