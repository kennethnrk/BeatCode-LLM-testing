test_cases = [
    {"input": 1, "output": 2},  # edge case, smallest n
    {"input": 2, "output": 1},  # smallest n > 1
    {"input": 3, "output": 2},  
    {"input": 4, "output": 3},  
    {"input": 5, "output": 2},  
    {"input": 6, "output": 5},  
    {"input": 7, "output": 2},  
    {"input": 8, "output": 7},  
    {"input": 9, "output": 2},  
    {"input": 13, "output": 3},  # example case
    {"input": 31, "output": 5},  
    {"input": 32, "output": 31}, 
    {"input": 4681, "output": 8},  # example case
    {"input": 100, "output": 3},  
    {"input": 127, "output": 2},  
    {"input": 1023, "output": 2},  
    {"input": 1024, "output": 4},  
    {"input": 1000000000000000000, "output": 999999999999999999},  # example case
    {"input": 15, "output": 2},  
    {"input": 4095, "output": 2}  
]
