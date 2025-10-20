def Solve(self, nums: list[int], target: int) -> int:
    # Initialize two pointers for the binary search.
    # 'low' represents the start of the current search space (inclusive).
    # 'high' represents the end of the current search space (inclusive).
    low = 0
    high = len(nums) - 1

    # Perform binary search. The loop continues as long as there's a valid search space.
    while low <= high:
        # Calculate the middle index.
        # Using this method to prevent potential integer overflow for very large low/high values.
        mid = low + (high - low) // 2

        # Compare the middle element with the target.
        if nums[mid] == target:
            # If target is found, return its index.
            return mid
        elif nums[mid] < target:
            # If the middle element is less than the target,
            # the target must be in the right half of the current search space.
            # Adjust 'low' to start searching from 'mid + 1'.
            low = mid + 1
        else: # nums[mid] > target
            # If the middle element is greater than the target,
            # the target must be in the left half of the current search space.
            # Adjust 'high' to end searching at 'mid - 1'.
            high = mid - 1

    # If the loop finishes, it means the target was not found in the array.
    # At this point, 'low' represents the index where the target should be inserted
    # to maintain the sorted order.
    return low