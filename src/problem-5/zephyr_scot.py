def Solve(nums):
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
