test_cases = [
    {"input": [3,3,5,0,0,3,1,4], "output": 6},  # Example case
    {"input": [1,2,3,4,5], "output": 4},        # Increasing sequence
    {"input": [7,6,4,3,1], "output": 0},        # Decreasing sequence
    {"input": [1], "output": 0},                # Single day (no transactions)
    {"input": [1,2], "output": 1},              # Two days, profit = 1
    {"input": [2,1], "output": 0},              # Two days, loss only
    {"input": [1,2,4,2,5,7,2,4,9,0], "output": 13},  # Two major profitable transactions
    {"input": [2,4,1,7,5,3,6,4,8], "output": 12},    # Two dips and rises
    {"input": [5,4,3,2,1,2,3,4,5], "output": 4},     # Profit only at end
    {"input": [1,2,4,2,5,7,2,4,9,0,9], "output": 17},# Strong double profit sequence
    {"input": [1,3,2,8,4,9], "output": 12},          # Buy low twice
    {"input": [2,1,2,0,1], "output": 1},             # Small ups and downs
    {"input": [1,2,3,1,2,3,1,2,3], "output": 4},     # Multiple small peaks
    {"input": [5,11,3,50,60,90], "output": 93},      # Big gap profits
    {"input": [3,2,6,5,0,3], "output": 7},           # Profit twice (buy low twice)
    {"input": [1,4,2,7], "output": 8},               # Two clear buy/sell points
    {"input": [3,3,3,3,3,3], "output": 0},           # Constant prices
    {"input": [1,2,3,4,5,4,3,2,1,2,3,4,5], "output": 8}, # Profit early & late
    {"input": [6,1,3,2,4,7], "output": 7},           # Overlapping profits
    {"input": [2,1,4,5,2,9,7], "output": 11}         # Multiple opportunities
]
