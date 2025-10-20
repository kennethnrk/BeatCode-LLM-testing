test_cases = [
    # Example test cases
    {"input": {"k": 2, "w": 0, "profits": [1,2,3], "capital": [0,1,1]}, "output": 4},
    {"input": {"k": 3, "w": 0, "profits": [1,2,3], "capital": [0,1,2]}, "output": 6},
    
    # Edge cases
    {"input": {"k": 0, "w": 0, "profits": [1,2,3], "capital": [0,1,2]}, "output": 0},  # k=0, can't do any projects
    {"input": {"k": 2, "w": 0, "profits": [], "capital": []}, "output": 0},  # no projects
    {"input": {"k": 2, "w": 5, "profits": [1,2,3], "capital": [10,10,10]}, "output": 0},  # can't afford any project
    {"input": {"k": 3, "w": 100, "profits": [1,2,3], "capital": [0,1,2]}, "output": 106},  # starting capital very high
    {"input": {"k": 1, "w": 0, "profits": [5], "capital": [0]}, "output": 5},  # single project, single k
    {"input": {"k": 1, "w": 1, "profits": [5], "capital": [2]}, "output": 1},  # single project but can't afford
    
    # Increasing size projects
    {"input": {"k": 3, "w": 0, "profits": [1,2,3,4], "capital": [0,0,1,2]}, "output": 9},
    {"input": {"k": 2, "w": 0, "profits": [5,10,15], "capital": [0,5,10]}, "output": 20},
    {"input": {"k": 3, "w": 0, "profits": [0,0,0], "capital": [0,0,0]}, "output": 0},  # all profits zero
    {"input": {"k": 3, "w": 1, "profits": [1,2,3], "capital": [2,2,2]}, "output": 1},  # can't afford any except initial low
    
    # All projects affordable from start
    {"input": {"k": 3, "w": 10, "profits": [1,2,3], "capital": [0,1,2]}, "output": 16},
    
    # Profits and capital the same
    {"input": {"k": 3, "w": 0, "profits": [1,2,3], "capital": [1,2,3]}, "output": 0},  # can't afford any at start
    {"input": {"k": 3, "w": 1, "profits": [1,2,3], "capital": [1,2,3]}, "output": 6},
    
    # Larger numbers
    {"input": {"k": 5, "w": 10, "profits": [20,30,40,50,60], "capital": [10,10,20,20,30]}, "output": 210},
    {"input": {"k": 3, "w": 5, "profits": [100,200,300], "capital": [0,50,200]}, "output": 605},
    
    # Only one project affordable
    {"input": {"k": 3, "w": 0, "profits": [10,20,30], "capital": [0,50,100]}, "output": 10},
    {"input": {"k": 2, "w": 10, "profits": [20,30,5], "capital": [20,10,15]}, "output": 40},
    
    # Large k, small projects
    {"input": {"k": 100, "w": 0, "profits": [1,2,3,4,5], "capital": [0,0,0,0,0]}, "output": 15},
    
    # Projects with same capital requirement
    {"input": {"k": 2, "w": 1, "profits": [5,10,3], "capital": [1,1,1]}, "output": 15},
    
    # Projects with same profit
    {"input": {"k": 2, "w": 1, "profits": [5,5,5], "capital": [0,1,2]}, "output": 10}
]
