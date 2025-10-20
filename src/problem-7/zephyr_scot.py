def Solve(nums1, nums2, k):
    I = len(nums1) - 1
    j = len(nums2) - 1
    result = [0] * k
    l = k - 1
    while I >= 0 and j >= 0 and l >= 0:
        if nums1[i] >= nums2[j]:
            result[l] = nums1[i]
            I -= 1
        else:
            result[l] = nums2[j]
            j -= 1
        l -= 1
    while I >= 0 and l >= 0:
        result[l] = nums1[i]
        I -= 1
        l -= 1
    while j >= 0 and l >= 0:
        result[l] = nums2[j]
        j -= 1
        l -= 1
    result = list(reversed(result))
    return result
