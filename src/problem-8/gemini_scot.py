import collections

def Solve(satisfaction: list[int]) -> int:
    # Step 1: Sort the satisfaction array in ascending order.
    # This is crucial for the greedy strategy. By sorting,
    # when we iterate from right to left, each 's' we consider
    # is the largest available remaining satisfaction value, and
    # if added, it will become the smallest element in our chosen subset.
    satisfaction.sort()

    n = len(satisfaction)
    
    # Step 2: Initialize variables.
    # `current_satisfaction_sum` tracks the sum of satisfaction levels
    # for all dishes currently included in our optimal subset.
    current_satisfaction_sum = 0
    
    # `current_like_time_sum` tracks the total like-time coefficient sum
    # for all dishes currently included in our optimal subset.
    # Initialized to 0, representing the option of cooking no dishes.
    current_like_time_sum = 0
    
    # Step 3 & 4: Iterate from right to left and apply greedy decision.
    # Loop from the largest satisfaction level (index n-1) down to the smallest (index 0).
    for i in range(n - 1, -1, -1):
        s = satisfaction[i]
        
        # Greedy Decision Check:
        # If adding the current dish 's' to the existing sum of satisfaction levels
        # (current_satisfaction_sum) results in a positive value, it means
        # the overall `current_like_time_sum` will increase.
        # This is based on the derivation: New_Total_Like_Time = Old_Total_Like_Time + (s + Old_Current_Satisfaction_Sum)
        if current_satisfaction_sum + s > 0:
            # Step 4b: If beneficial, include this dish.
            # Update the sum of satisfaction levels. 's' is now part of the selected dishes.
            current_satisfaction_sum += s
            
            # Update the total like-time coefficient sum.
            # The total sum increases by the new `current_satisfaction_sum`
            # (which is `s` plus the sum of previously chosen dishes).
            current_like_time_sum += current_satisfaction_sum
        else:
            # Step 4c: If `current_satisfaction_sum + s <= 0`, adding 's' would not
            # increase the total like-time sum. Since 's' is the largest
            # of the remaining unchosen dishes (due to right-to-left iteration),
            # adding any smaller dish would also not be beneficial.
            # Therefore, we break the loop as we've found our maximum.
            break
            
    # Step 5: Return `current_like_time_sum`.
    # At this point, `current_like_time_sum` holds the maximum possible
    # like-time coefficient sum. If no dishes were chosen (e.g., all
    # satisfaction levels were negative and the loop broke immediately),
    # it correctly remains 0.
    return current_like_time_sum