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
    {"input": 1690, "output": 2123366400}  # LeetCode upper bound
]
