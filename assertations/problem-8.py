def assert_problem_8(result, nums1, nums2, k):
    """
    Verify that `result` is a valid solution for `Solve(nums1, nums2, k)`.

    This checks:
    - basic constraints (length and digit bounds),
    - subsequence order preservation with respect to `nums1` and `nums2`,
    - and lexicographical maximality over all valid splits of length `k`.
    """
    # Function signature for context: def Solve(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    # Let 'result' be the array returned by Solve(nums1, nums2, k).

    # --- Basic Constraints and Properties ---
    assert len(result) == k
    assert all(0 <= digit <= 9 for digit in result)

    # --- Subsequence Property (Relative Order Preservation) ---
    # Assertion 1: Relative Order Preservation for nums1
    # Checks if the digits in 'result' that conceptually came from 'nums1' appear in the correct relative order.
    assert (
        (
            i_1 := -1,
            last_i1 := -1,
            all(
                (
                    # Find the next index i_1 in nums1 greater than last_i1 that matches result[i_r]
                    # This simulates finding the required digit in nums1 to satisfy the ordering.
                    i_1 := next(
                        (
                            j for j in range(last_i1 + 1, len(nums1))
                            if result[i_r] == nums1[j]
                        ),
                        -1,  # If no match is found, i_1 remains -1
                    ),
                    # If a match is found, update last_i1 and proceed. If no match is found,
                    # the result *cannot* be formed by preserving the order of the current result[i_r] *if* we assume it comes from nums1.
                    # Since we don't know the exact split, the combined failure to find a path in *either* nums1 or nums2
                    # over the whole sequence check (not just one digit) implies the sequence is invalid.
                    # A robust check is to ensure that for *some* path through result, the order is preserved in both.
                    # The given structure is a necessary condition: if result is the answer, a path must exist through nums1 and nums2.
                    i_1 != -1 and (last_i1 := i_1) >= 0,
                )
                for i_r in range(k)
            ),
        )
    )

    # Assertion 2: Relative Order Preservation for nums2
    # Checks if the digits in 'result' that conceptually came from 'nums2' appear in the correct relative order.
    assert (
        (
            i_2 := -1,
            last_i2 := -1,
            all(
                (
                    i_2 := next(
                        (
                            j for j in range(last_i2 + 1, len(nums2))
                            if result[i_r] == nums2[j]
                        ),
                        -1,
                    ),
                    i_2 != -1 and (last_i2 := i_2) >= 0,
                )
                for i_r in range(k)
            ),
        )
    )

    # --- Maximality Property ---
    # Assertion 3: Lexicographical Maximality
    # Checks that for all possible valid splits (len1, len2) where len1 + len2 = k,
    # the lexicographically maximum merge of the max-length-len1 subsequence of nums1 and
    # the max-length-len2 subsequence of nums2 is less than or equal to 'result'.

    # Helper logic defined internally for finding max subsequence (s1, s2) and max merge.
    # 1. Function to find the max subsequence of length 'l' from 'arr' (Greedy Monotonic Stack)
    def find_max_subsequence(arr, l):
        if l == 0:
            return []
        stack = []
        for i, digit in enumerate(arr):
            # Pop smaller digits if they can be replaced by the current larger digit,
            # while still ensuring enough remaining digits to meet the target length 'l'.
            while stack and stack[-1] < digit and len(stack) + (len(arr) - i) > l:
                stack.pop()
            if len(stack) < l:
                stack.append(digit)
        return stack[:l]

    # 2. Function to find the max merge of two sequences (s1, s2)
    def find_max_merge(a, b):
        res = []
        i, j = 0, 0
        while i < len(a) or j < len(b):
            # Use list comparison for lexicographical check (a[i:] > b[j:] means 'a' wins)
            # Python's list comparison works correctly for this greedy choice.
            if i < len(a) and (j == len(b) or a[i:] > b[j:]):
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        return res

    # Iterate over all possible length splits
    assert all(
        (
            len1 + len2 == k
            and 0 <= len1 <= len(nums1)
            and 0 <= len2 <= len(nums2)
        )
        and (
            s1 := find_max_subsequence(nums1, len1),
            s2 := find_max_subsequence(nums2, len2),
            merged_sub := find_max_merge(s1, s2),
            # The result must be lexicographically greater than or equal to the maximum possible
            # number formed by any valid split.
            merged_sub <= result,
        )
        for len1 in range(k + 1)
        for len2 in range(k + 1)
        if len1 + len2 == k
        and 0 <= len1 <= len(nums1)
        and 0 <= len2 <= len(nums2)
    )


