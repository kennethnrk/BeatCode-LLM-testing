test_cases = [
    {"input": [1, 3, 5], "output": 1},  # basic increasing order
    {"input": [2, 2, 2, 0, 1], "output": 0},  # classic rotation with duplicates
    {"input": [1, 1, 1, 1, 1], "output": 1},  # all identical elements
    {"input": [10], "output": 10},  # single element
    {"input": [2, 2, 2, 2, 2, 2], "output": 2},  # all duplicates
    {"input": [3, 4, 5, 1, 2], "output": 1},  # rotated sorted array
    {"input": [4, 5, 6, 7, 0, 1, 2], "output": 0},  # typical rotated array
    {"input": [0, 1, 2, 4, 5, 6, 7], "output": 0},  # no rotation
    {"input": [2, 3, 4, 5, 1, 2], "output": 1},  # rotation with duplicates at ends
    {"input": [5, 6, 1, 2, 3, 4], "output": 1},  # rotated mid-way
    {"input": [1, 2, 3, 4, 5, 6, 7], "output": 1},  # fully sorted (no rotation)
    {"input": [2, 2, 2, 3, 1, 2], "output": 1},  # duplicates on both sides of min
    {"input": [1, 1, 3, 1], "output": 1},  # min repeated after rotation
    {"input": [3, 1, 3], "output": 1},  # minimal 3-element case with duplicates
    {"input": [2, 2, 2, 0, 0, 1, 1], "output": 0},  # multiple duplicate minima
    {"input": [5, 5, 1, 2, 3, 4, 5], "output": 1},  # duplicate leading elements
    {"input": [4, 4, 5, 6, 7, 0, 1, 2, 4], "output": 0},  # duplicate near pivot
    {"input": [1, 3, 3], "output": 1},  # simple rotation, duplicates end
    {"input": [3, 3, 3, 3, 3, 3, 1, 3], "output": 1},  # all same except one min
    {"input": [1, 2, 3, 4, 5, 0], "output": 0}  # rotation by n-1
]
