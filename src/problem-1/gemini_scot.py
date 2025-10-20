def Solve(n: int) -> int:
    """
    Finds the nth ugly number.

    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Args:
        n: The desired position of the ugly number (e.g., 10 for the 10th ugly number).

    Returns:
        The nth ugly number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    # ugly_numbers will store the sequence of ugly numbers in increasing order.
    # The first ugly number is 1.
    ugly_numbers = [1]
    
    # Pointers for tracking the next multiple of 2, 3, and 5
    # p2, p3, p5 store the indices of the ugly_numbers array.
    # ugly_numbers[p2] * 2 is the next candidate multiple of 2, and so on.
    p2 = 0
    p3 = 0
    p5 = 0
    
    # We already have the 1st ugly number, so we need to generate n-1 more.
    for _ in range(1, n):
        # Calculate the next potential ugly numbers by multiplying the
        # current pointed ugly number by 2, 3, and 5.
        next_multiple_of_2 = ugly_numbers[p2] * 2
        next_multiple_of_3 = ugly_numbers[p3] * 3
        next_multiple_of_5 = ugly_numbers[p5] * 5
        
        # The next ugly number is the minimum of these three candidates.
        next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        
        # Add the new ugly number to our list.
        ugly_numbers.append(next_ugly)
        
        # Increment the pointers for any candidate that resulted in the next_ugly.
        # This is crucial for handling duplicates (e.g., 6 = 2*3 = 3*2)
        # and advancing the correct sequence.
        if next_ugly == next_multiple_of_2:
            p2 += 1
        if next_ugly == next_multiple_of_3:
            p3 += 1
        if next_ugly == next_multiple_of_5:
            p5 += 1
            
    # The nth ugly number is at index n-1 (due to 0-based indexing).
    return ugly_numbers[n - 1]