def Solve(i):
    if i == 0:
        return satisfaction[i] * time[i]

    if (i, True) in memo or (i, False) in memo:
        return memo[(i, True)] if memo[(i, True)] > memo[(i, False)] else memo[(i, False)]

    max_like_time_coefficient = 0
    current_like_time_coefficient = 0

    for j in range(i):
        like_time_coefficient = satisfaction[j] * time[j] + solve(j)
        if like_time_coefficient > current_like_time_coefficient:
            current_like_time_coefficient = like_time_coefficient

    memo[(i, True)] = max(max_like_time_coefficient, current_like_time_coefficient)
    memo[(i, False)] = max_like_time_coefficient

    return memo[(i, True)]

def reduce_dishes(satisfaction):
    time = [1] * len(satisfaction)
    memo = {}
    return solve(len(satisfaction) - 1)