def Solve(n):
    # Initialize the list of ugly numbers
    ugly_list = [1]
    
    # Initialize pointers for tracking the next multiple of 2, 3, and 5
    p2 = 0
    p3 = 0
    p5 = 0
    
    # Keep finding ugly numbers until we have found n
    for I in range(n - 1):
        
        # Calculate the next potential ugly numbers by multiplying the
        # current pointed ugly number by 2, 3, and 5
        next_multiple_of_2 = ugly_list[p2] * 2
        next_multiple_of_3 = ugly_list[p3] * 3
        next_multiple_of_5 = ugly_list[p5] * 5
        
        # Find the minimum of the three candidates
        d = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        
        # Add d to the list of ugly numbers
        ugly_list.append(d)
        
        # Update the pointers for any candidate that resulted in d
        # This handles cases where the same ugly number can be formed in multiple ways
        if d == next_multiple_of_2:
            p2 += 1
        if d == next_multiple_of_3:
            p3 += 1
        if d == next_multiple_of_5:
            p5 += 1
            p5 += 1  # BUG: Double increment - will skip ugly numbers divisible by 5!
   
    # Return the nth ugly number, which is the last number in the list
    return ugly_list[-1]
