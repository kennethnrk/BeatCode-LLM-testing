import bisect

def Solve(envelopes: list[list[int]]) -> int:
    # Handle the edge case where no envelopes are provided.
    if not envelopes:
        return 0

    # Step 1: Sort the envelopes
    # Sort primarily by width (x[0]) in ascending order.
    # If widths are equal, sort by height (-x[1]) in descending order.
    # This ensures that envelopes with the same width cannot be part of the same
    # increasing subsequence of heights, effectively handling the strict width condition.
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # Step 2: Extract heights
    # Create a list containing only the heights from the sorted envelopes.
    heights = [env[1] for env in envelopes]

    # Step 3: Find the Longest Increasing Subsequence (LIS) of the heights
    # 'tails' will store the smallest ending element of all increasing subsequences
    # of length (index + 1) found so far.
    tails = []

    for h in heights:
        # Use bisect_left to find the index 'idx' where 'h' can be inserted
        # in 'tails' to maintain sorted order.
        # 'idx' will be the first index such that tails[idx] >= h.
        idx = bisect.bisect_left(tails, h)

        # If 'idx' is equal to the current length of 'tails', it means 'h' is
        # strictly greater than all elements currently in 'tails'.
        # So, we extend the longest increasing subsequence found so far by appending 'h'.
        if idx == len(tails):
            tails.append(h)
        # Otherwise, 'h' is not strictly greater than all elements.
        # We found an increasing subsequence of length 'idx + 1' ending with tails[idx].
        # By replacing tails[idx] with 'h', we form an increasing subsequence of
        # the same length 'idx + 1' but with a potentially smaller tail 'h'.
        # A smaller tail is more favorable as it allows more subsequent elements
        # to extend this subsequence further.
        else:
            tails[idx] = h
    
    # The final length of the 'tails' list represents the length of the LIS,
    # which is the maximum number of envelopes that can be Russian dolled.
    return len(tails)

