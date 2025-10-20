def Solve(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    m, n = len(nums1), len(nums2)
    max_overall_number = [] # Initialize with an empty list, which is lexicographically smallest

    # Helper function 1: Get the lexicographically largest subsequence of a given length
    # from a single array. Uses a monotonic stack approach.
    def get_max_subsequence(nums: list[int], length: int) -> list[int]:
        if length == 0:
            return []
        
        # Number of elements to drop from `nums` to get `length` elements
        to_drop = len(nums) - length
        
        stack = []
        for digit in nums:
            # While stack is not empty, current digit is greater than the top of the stack,
            # AND we still have elements we can afford to drop.
            while stack and digit > stack[-1] and to_drop > 0:
                stack.pop()
                to_drop -= 1
            stack.append(digit)
        
        # Trim the stack to the exact desired length, as `to_drop` might have become 0
        # before all digits were processed, leading to a stack longer than `length`.
        return stack[:length]

    # Helper function 2: Determine which suffix (from idx1 or idx2) is lexicographically greater
    def greater(arr1: list[int], idx1: int, arr2: list[int], idx2: int) -> bool:
        while idx1 < len(arr1) and idx2 < len(arr2):
            if arr1[idx1] > arr2[idx2]:
                return True
            if arr1[idx1] < arr2[idx2]:
                return False
            idx1 += 1
            idx2 += 1
        
        # If one array runs out, the one that still has elements is greater (e.g., [6,7] > [6]).
        # This means if arr1 still has elements, it's longer and thus greater.
        return idx1 < len(arr1)

    # Helper function 3: Merge two arrays to form the lexicographically largest number
    def merge(sub1: list[int], sub2: list[int]) -> list[int]:
        result = []
        i, j = 0, 0
        
        # Loop until both arrays are exhausted
        while i < len(sub1) or j < len(sub2):
            if i < len(sub1) and j < len(sub2):
                # Use the 'greater' helper to decide which digit to pick
                if greater(sub1, i, sub2, j):
                    result.append(sub1[i])
                    i += 1
                else:
                    result.append(sub2[j])
                    j += 1
            elif i < len(sub1): # sub2 is exhausted, append remaining from sub1
                result.extend(sub1[i:])
                break
            else: # sub1 is exhausted, append remaining from sub2
                result.extend(sub2[j:])
                break
        return result

    # Main logic: Iterate through all possible splits of k digits
    # `i`: number of digits to take from nums1
    # `j`: number of digits to take from nums2 (j = k - i)
    #
    # The loop range for `i` ensures:
    # 1. `i >= 0` (cannot take negative digits from nums1)
    # 2. `i <= m` (cannot take more digits than available in nums1)
    # 3. `j >= 0` => `k - i >= 0` => `i <= k` (cannot leave negative digits for nums2)
    # 4. `j <= n` => `k - i <= n` => `i >= k - n` (cannot take too few from nums1, leaving too many for nums2)
    # Combining these: `max(0, k - n) <= i <= min(k, m)`
    
    # Note: The `range` function's second argument is exclusive, so we add 1 to `min(k, m)`
    for i in range(max(0, k - n), min(k, m) + 1):
        j = k - i # Calculate remaining digits for nums2
        
        sub1_max = get_max_subsequence(nums1, i)
        sub2_max = get_max_subsequence(nums2, j)
        
        current_merged_number = merge(sub1_max, sub2_max)
        
        # Python's list comparison works lexicographically,
        # allowing direct comparison of digit arrays.
        if current_merged_number > max_overall_number:
            max_overall_number = current_merged_number
    
    return max_overall_number