test_cases = [
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
]
