test_cases = [
    {"input": {"nums": [1,3,5,6], "target": 5}, "output": 2},
    {"input": {"nums": [1,3,5,6], "target": 2}, "output": 1},
    {"input": {"nums": [1,3,5,6], "target": 7}, "output": 4},
    {"input": {"nums": [1,3,5,6], "target": 0}, "output": 0},
    {"input": {"nums": [1], "target": 0}, "output": 0},
    {"input": {"nums": [1], "target": 2}, "output": 1},
    {"input": {"nums": [], "target": 5}, "output": 0},  # edge case: empty array
    {"input": {"nums": [2,4,6,8,10], "target": 6}, "output": 2},
    {"input": {"nums": [2,4,6,8,10], "target": 5}, "output": 2},
    {"input": {"nums": [2,4,6,8,10], "target": 11}, "output": 5},
    {"input": {"nums": [2,4,6,8,10], "target": 1}, "output": 0},
    {"input": {"nums": [10,20,30,40,50], "target": 35}, "output": 3},
    {"input": {"nums": [10,20,30,40,50], "target": 10}, "output": 0},
    {"input": {"nums": [10,20,30,40,50], "target": 50}, "output": 4},
    {"input": {"nums": [10,20,30,40,50], "target": 60}, "output": 5},
    {"input": {"nums": [-10,-5,0,5,10], "target": -6}, "output": 1},
    {"input": {"nums": [-10,-5,0,5,10], "target": 5}, "output": 3},
    {"input": {"nums": [-10,-5,0,5,10], "target": -10}, "output": 0},
    {"input": {"nums": [-10,-5,0,5,10], "target": 15}, "output": 5},
    {"input": {"nums": [1,3,5,7,9,11,13,15,17,19], "target": 14}, "output": 7}
]
