test_cases = [
    # Small and base cases
    {"input": 1, "output": 1},           # base case
    {"input": 2, "output": 2},
    {"input": 3, "output": 3},
    {"input": 4, "output": 4},
    {"input": 5, "output": 5},

    # Transition and prime-factor mix regions
    {"input": 6, "output": 6},           # 2*3
    {"input": 7, "output": 8},           # power of 2
    {"input": 8, "output": 9},           # power of 3
    {"input": 9, "output": 10},          # includes factor 5
    {"input": 10, "output": 12},

    # Mid-range sanity checks
    {"input": 11, "output": 15},
    {"input": 12, "output": 16},
    {"input": 13, "output": 18},
    {"input": 14, "output": 20},
    {"input": 15, "output": 24},
    {"input": 20, "output": 36},

    # Larger boundary and performance tests
    {"input": 100, "output": 1536},
    {"input": 150, "output": 5832},
    {"input": 500, "output": 61440},
    {"input": 1690, "output": 2123366400},  # LeetCode upper bound
    
    # Additional coverage tests for different multiplier paths
    # These tests exercise all three branches (p2, p3, p5 updates)
    {"input": 16, "output": 18},         # Tests p2 path
    {"input": 17, "output": 20},         # Tests p2 path  
    {"input": 21, "output": 24},        # Tests p3 path
    {"input": 22, "output": 27},         # Tests p3 path
    {"input": 23, "output": 25},         # Tests p5 path
    {"input": 24, "output": 27},        # Tests p5 path
    {"input": 25, "output": 30},        # Tests tie handling (multiple branches)
    {"input": 26, "output": 32},        # Tests various paths
    {"input": 30, "output": 36},        # More iterations
    {"input": 35, "output": 45},         # Different multiplier sequences
    {"input": 40, "output": 48},         # Tests various branches
    {"input": 45, "output": 54},        # More iterations
    {"input": 50, "output": 72},         # Complex update sequence
    {"input": 55, "output": 72},        # Tests update logic
    {"input": 60, "output": 80},        # Tests all three update paths
    {"input": 65, "output": 80},        # More coverage
    {"input": 70, "output": 90},        # More coverage
    {"input": 75, "output": 90},        # Different sequences
    {"input": 80, "output": 100},       # Different patterns
]
