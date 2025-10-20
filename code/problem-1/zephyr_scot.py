def Solve(n):
    # Initialize the list of ugly numbers
    ugly_list = [1]
    
    # Initialize variables for the last three numbers in the list
    a = 1
    b = 1
    c = 1
    
    # Keep finding ugly numbers until we have found n
    for I in range(n - 1):
        
        # Find the minimum of the last three numbers and their multiples by 2, 3, and 5
        d = min(a * 2, b * 3, c * 5)
        
        # Add d to the list of ugly numbers
        ugly_list.append(d)
        
        # Update the variables for the last three numbers in the list
        if d == a * 2:
            a = b
        if d == b * 3:
            b = c
        if d == c * 5:
            c = ugly_list[-1]
   
    # Return the nth ugly number, which is the last number in the list
    return ugly_list[-1]
