test_cases = [
    # Edge case: empty list (for coverage of line 3)
    {"input": [], "output": 0},
    
    # Basic examples
    {"input": [[5,4],[6,4],[6,7],[2,3]], "output": 3},
    {"input": [[1,1],[1,1],[1,1]], "output": 1},

    # Edge case: only one envelope
    {"input": [[2,3]], "output": 1},

    # Increasing sequence of envelopes
    {"input": [[1,1],[2,2],[3,3],[4,4]], "output": 4},

    # Decreasing order (should sort internally)
    {"input": [[4,4],[3,3],[2,2],[1,1]], "output": 4},

    # No nesting possible (widths increase, heights same)
    {"input": [[1,5],[2,5],[3,5],[4,5]], "output": 1},

    # Mixed values but no nesting possible
    {"input": [[4,6],[4,5],[4,7],[4,8]], "output": 1},

    # Some nesting possible
    {"input": [[5,4],[6,10],[6,7],[7,8],[2,3]], "output": 4},

    # Same width, different heights
    {"input": [[3,4],[3,5],[3,6],[3,3]], "output": 1},

    # All identical except one slightly larger
    {"input": [[2,3],[2,3],[3,4]], "output": 2},

    # Large random values
    {"input": [[100,200],[200,300],[300,400],[250,350]], "output": 3},

    # Some envelopes with same width and height mix
    {"input": [[1,3],[2,3],[3,3],[3,4],[4,5]], "output": 3},

    # Non-continuous nesting
    {"input": [[1,1],[3,3],[6,6],[4,5]], "output": 3},

    # Large numbers, but limited nesting
    {"input": [[10**6,10**6],[10**6-1,10**6-1],[10**6-2,10**6-3]], "output": 3},

    # Random order, nested possible
    {"input": [[8,9],[5,4],[6,7],[2,3],[10,11],[9,10]], "output": 5},

    # Equal widths, strictly increasing heights (only one valid)
    {"input": [[5,1],[5,2],[5,3],[5,4]], "output": 1},

    # Large input with alternating heights (nested every other)
    {"input": [[1,10],[2,9],[3,8],[4,7],[5,6],[6,5],[7,4],[8,3],[9,2],[10,1]], "output": 1},

    # Zigzag pattern
    {"input": [[1,1],[2,3],[3,2],[4,4],[5,3]], "output": 3},

    # All envelopes same size except one smallest
    {"input": [[2,2],[2,2],[2,2],[1,1]], "output": 2},

    # Large spread with random nesting possible
    {"input": [[4,5],[4,6],[6,7],[2,3],[1,1],[5,4],[7,8],[3,4]], "output": 5},
    
    # Additional coverage tests
    # Two envelopes - both cases
    {"input": [[1,1],[2,2]], "output": 2},      # Can nest
    {"input": [[2,2],[1,1]], "output": 2},      # Can nest (reversed)
    {"input": [[1,2],[2,1]], "output": 1},      # Cannot nest (width/height conflict)
    
    # Three envelopes - various patterns
    {"input": [[1,1],[2,2],[3,3]], "output": 3},  # All can nest
    {"input": [[3,3],[2,2],[1,1]], "output": 3},  # All can nest (reversed)
    {"input": [[1,3],[2,2],[3,1]], "output": 1},  # None can nest properly
    
    # Cases to test inner loop branches
    {"input": [[1,1],[3,3],[2,2]], "output": 3},  # Out of order but all nest
    {"input": [[2,2],[1,1],[3,3]], "output": 3},  # Different order
    
    # Cases where condition is false (envelopes[j][0] >= envelopes[i][0] or envelopes[j][1] >= envelopes[i][1])
    {"input": [[5,5],[3,6],[4,4]], "output": 2},  # Width condition false
    {"input": [[5,5],[6,3],[4,4]], "output": 2},  # Height condition false
    {"input": [[5,5],[5,5],[4,4]], "output": 2},  # Both equal (condition false)
    
    # Cases to test max() calls
    {"input": [[1,1],[2,2],[1,2],[2,1]], "output": 2},  # Tests max logic
    {"input": [[1,1],[3,3],[2,2],[4,4]], "output": 4},  # Tests max with multiple options
    
    # Edge cases for loop boundaries
    {"input": [[1,1]], "output": 1},             # Single envelope (I=1, len=1, loop doesn't run)
    {"input": [[1,1],[2,2]], "output": 2},      # Two envelopes (I=1, j=0)
    
    # Cases with many envelopes to test nested loops
    {"input": [[1,1],[2,2],[3,3],[4,4],[5,5]], "output": 5},  # All nest
    {"input": [[5,5],[4,4],[3,3],[2,2],[1,1]], "output": 5},  # All nest reversed
    
    # Cases to test recursive solve() calls with different subarrays
    {"input": [[1,1],[3,3],[2,2],[4,4]], "output": 4},  # Tests solve(envelopes[j:i+1])
    {"input": [[2,2],[1,1],[4,4],[3,3]], "output": 4},  # Different subarray patterns
    
    # Cases where maxEnvelopes updates in different branches
    {"input": [[1,5],[2,4],[3,3],[4,2],[5,1]], "output": 1},  # No nesting
    {"input": [[1,1],[2,1],[3,1],[4,1]], "output": 1},        # Same height, increasing width
    
    # More complex nesting patterns
    {"input": [[1,1],[2,3],[3,2],[4,4],[5,5]], "output": 3},  # Mixed pattern
    {"input": [[2,3],[1,1],[4,5],[3,2],[5,4]], "output": 3},  # Complex ordering
    
    # Cases to ensure all code paths in nested loops are tested
    {"input": [[1,10],[2,9],[3,8],[4,7],[5,6]], "output": 1},  # Decreasing heights
    {"input": [[10,1],[9,2],[8,3],[7,4],[6,5]], "output": 1},  # Increasing heights, decreasing widths
]
