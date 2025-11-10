import math

def calculate_sum_of_powers(k, m, N_val):
    current_sum = 0
    current_term = 1
    
    for i in range(m):
        if current_sum > N_val - current_term:
            return N_val + 1
        current_sum += current_term
        
        if i < m - 1:
            if current_term > N_val // k:
                return N_val + 1
            current_term *= k
    
    return current_sum

def Solve(n):
    N_val = int(n)
    
    if N_val == 1:
        return 2
    if N_val == 2:
        return 1
    
    max_m = math.floor(math.log2(N_val + 1))
    
    for m in range(max_m, 1, -1):
        low = 2
        high = int(math.pow(N_val, 1.0 / (m - 1))) + 2
        high = min(high, N_val - 1)
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if mid < 2:
                low = 2
                continue
            
            current_N_sum = calculate_sum_of_powers(mid, m, N_val)
            
            if current_N_sum == N_val:
                return mid
            elif current_N_sum < N_val:
                low = mid + 1
            else:
                high = mid - 1
    
    return N_val - 1