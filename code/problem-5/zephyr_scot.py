def find_min(nums):
    left, right = 0, len(nums) - 1
    min_idx = left
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= nums[right]:
            right = mid
            if nums[left] > nums[right]:
                min_idx = right
        else:
            left = mid + 1
            if nums[left] <= nums[right]:
                min_idx = left
    return nums[min_idx]

# Example usage
arr = [2, 2, 2, 0, 1]
print(find_min(arr))  # Output: 0
