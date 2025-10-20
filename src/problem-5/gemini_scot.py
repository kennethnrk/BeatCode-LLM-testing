def Solve(nums: list[int]) -> int:
    low = 0
    high = len(nums) - 1

    # The loop continues as long as there is more than one element to consider.
    while low < high:
        mid = low + (high - low) // 2

        # Case 1: nums[mid] is less than nums[high]
        # This indicates that the right part (from mid to high) is sorted or
        # nums[mid] itself is the minimum. The minimum cannot be in (mid, high].
        # So, we can safely narrow our search to the left half, including mid.
        if nums[mid] < nums[high]:
            high = mid
        
        # Case 2: nums[mid] is greater than nums[high]
        # This indicates that the minimum element lies in the right half
        # (from mid + 1 to high). The rotation point is definitely after mid.
        # nums[mid] cannot be the minimum.
        elif nums[mid] > nums[high]:
            low = mid + 1
        
        # Case 3: nums[mid] is equal to nums[high]
        # This is the tricky part due to duplicates.
        # We cannot determine for sure if the minimum is to the left or right of mid
        # based solely on this comparison (e.g., [3,1,3,3,3] vs [3,3,3,1,3]).
        # To ensure we don't discard the minimum, we safely decrement the high pointer.
        # This effectively shrinks the search space from the right.
        # In the worst case (e.g., [1,1,1,1,0,1,1,1]), this degenerates to O(N) complexity.
        else: # nums[mid] == nums[high]
            high -= 1
    
    # When the loop terminates, 'low' and 'high' will point to the same index,
    # which contains the minimum element.
    return nums[low]