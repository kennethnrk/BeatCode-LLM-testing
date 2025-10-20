def Solve(s):
    # Step 1: Split the string into an array of summands
    summands = s.split('+')
    
    # Step 2: Sort the array in non-decreasing order
    summands.sort(key=lambda x: int(x))
    
    # Step 3: Join the sorted array back into a string
    return '+'.join(summands)
