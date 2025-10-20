import math

# The helper function remains the core logic for calculating the geometric series sum
def calculate_sum_of_powers(k: int, m: int, N_val: int) -> int:
    """
    Calculates the sum 1 + k + k^2 + ... + k^(m-1).
    Returns N_val + 1 if the sum would exceed N_val, preventing overflow.
    """
    current_sum = 0
    current_term = 1  # Represents k^0, k^1, k^2, etc.

    for i in range(m):
        # 1. Check for sum overflow: current_sum + current_term > N_val
        # Since current_term >= 1, we can check N_val - current_sum < current_term
        if current_sum > N_val - current_term:
            return N_val + 1  # Signal k is too large
        current_sum += current_term

        # 2. Prepare for the next term, check for current_term * k overflow:
        if i < m - 1: # Only multiply if there's a next term
            # If current_term > N_val // k, then current_term * k > N_val
            # N_val // k is safe since k >= 2.
            if current_term > N_val // k:
                return N_val + 1  # Signal k is too large
            current_term *= k
    
    return current_sum

def solve(N_val: int) -> int:
    """
    Finds the smallest good base k for a given integer N (from n_str).
    A good base k means N's representation in base k is all ones.
    """

    # Base k = N_val - 1 is always a good base for length m=2 (N = 1 + k^1).
    if N_val < 3:
        return N_val - 1

    # 1. Determine the maximum possible length m (number of ones).
    # N ~ 2^m => m ~ log2(N).
    # We use N+1 for safety since N = k^(m-1) + ... + 1 >= 2^m - 1
    max_m = math.floor(math.log2(N_val + 1)) 

    # 2. Iterate through m (length) downwards from max_m to 2.
    # We iterate downwards because the goal is to find the smallest k, and a 
    # larger m generally results in a smaller k (e.g., 7 in base 2 is 111 (m=3, k=2); 
    # 7 in base 6 is 11 (m=2, k=6)).
    for m in range(max_m, 1, -1):
        low = 2 # The smallest possible base k
        
        # 3. Calculate a tighter upper bound for k.
        # N_val > k^(m-1) => k < N_val^(1/(m-1))
        high = int(math.pow(N_val, 1.0 / (m - 1))) + 2
        high = min(high, N_val - 1) # k cannot be N_val or greater
        
        # 4. Binary search for k in the range [low, high].
        while low <= high:
            mid = low + (high - low) // 2

            if mid < 2:
                low = 2
                continue
            
            # Use the helper function to check the sum
            current_N_sum = calculate_sum_of_powers(mid, m, N_val)

            if current_N_sum == N_val:
                # Found the smallest k for this m. Since m decreases, 
                # this is the smallest overall good base.
                return mid
            elif current_N_sum < N_val:
                # The base k (mid) is too small, need a larger base
                low = mid + 1
            else: # current_N_sum > N_val (or overflowed)
                # The base k (mid) is too large, need a smaller base
                high = mid - 1
    
    # Fallback/Default for m=2: k = N_val - 1. This should be hit by the loop, 
    # but serves as the final result as in the original logic.
    return N_val - 1