def Solve(satisfaction: list[int]) -> int:
    satisfaction.sort()
    
    n = len(satisfaction)
    current_satisfaction_sum = 0
    current_like_time_sum = 0
    
    for i in range(n - 1, -1, -1):
        s = satisfaction[i]
        if current_satisfaction_sum + s > 0:
            current_satisfaction_sum += s
            current_like_time_sum += current_satisfaction_sum
        else:
            break
    
    return current_like_time_sum