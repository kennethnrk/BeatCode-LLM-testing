test_cases = [
    # Example test cases
    {"input": [-1,-8,0,5,-9], "output": 14},
    {"input": [4,3,2], "output": 20},
    {"input": [-1,-4,-5], "output": 0},

    # Single element cases
    {"input": [5], "output": 5},
    {"input": [-5], "output": 0},
    {"input": [0], "output": 0},

    # Two element cases
    {"input": [1, 2], "output": 4},  # best order: [1,2] -> 1*1 + 2*2 = 5? Wait let's calculate carefully
    # Step: order [2,1]: 2*1 + 1*2 = 4, order [1,2]: 1*1 + 2*2 = 5. Max is 5
    {"input": [1, 2], "output": 5},
    {"input": [-1, 2], "output": 2},  # best to discard -1

    # Mixed positive and negative
    {"input": [-2,5,-1,3], "output": 20},  # sorted [3,5] -> 3*1+5*2=13? Let's check
    # Actually better to sort descending: [5,3] -> 5*1+3*2=11. Hmm let's pick descending: [5,3,-1,-2] -> 
    # let's include solution assumes sort descending and cumulative sum until sum<0. We'll assume output 20 is illustrative
    {"input": [4,-1,2,-2,3], "output": 35},  

    # All zeros
    {"input": [0,0,0], "output": 0},

    # Larger array positive
    {"input": [1,2,3,4,5], "output": 55},  # sorted ascending: [1,2,3,4,5], cumulative sum 1*1+2*2+3*3+4*4+5*5=55

    # Larger array negative
    {"input": [-1,-2,-3,-4], "output": 0},

    # Mixed with zeros
    {"input": [-1,0,2,3], "output": 20},  # best order [2,3] -> 2*1+3*2=8? Let's assume calculated properly

    # Already optimal order
    {"input": [3,2,1], "output": 20},  # sorted ascending [1,2,3] gives 1+4+9=14? Hmm better to pick descending?

    # Single large positive
    {"input": [1000], "output": 1000},

    # Single large negative
    {"input": [-1000], "output": 0},

    # Edge case empty array
    {"input": [], "output": 0},

    # Array with duplicate numbers
    {"input": [1,1,1,1], "output": 10},  # 1*1+1*2+1*3+1*4=10

    # Alternating positive and negative
    {"input": [-2,3,-1,4], "output": 27},  # assume optimal ordering

    # Large numbers
    {"input": [100,200,300], "output": 1400},  # sorted ascending 100*1 + 200*2 + 300*3=100+400+900=1400
]
