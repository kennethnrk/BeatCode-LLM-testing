def solve(s):
    # Step 1: Split the string into an array of summands
    summands = s.split('+')
    
    # Step 2: Sort the array in non-decreasing order
    summands.sort(key=lambda x: int(x))
    
    # Step 3: Join the sorted array back into a string
    return '+'.join(summands)

# Example usage:
print(solve("3+2+1"))  # Output: "1+2+3"
print(solve("1+1+3+1+3"))  # Output: "1+1+1+3+3"
print(solve("2"))  # Output: "2"
