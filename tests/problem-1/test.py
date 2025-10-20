test_cases = [
    # --- Basic happy cases ---
    {"input": "3+2+1", "output": "1+2+3"},
    {"input": "1+1+3+2", "output": "1+1+2+3"},
    {"input": "2+3+1+3+2", "output": "1+2+2+3+3"},
    {"input": "1+3+3+2+1", "output": "1+1+2+3+3"},

    # --- Already sorted ---
    {"input": "1+1+2+2+3", "output": "1+1+2+2+3"},
    {"input": "1", "output": "1"},
    {"input": "1+2", "output": "1+2"},
    {"input": "1+2+3", "output": "1+2+3"},

    # --- All same numbers ---
    {"input": "1+1+1+1", "output": "1+1+1+1"},
    {"input": "2+2+2", "output": "2+2+2"},
    {"input": "3+3", "output": "3+3"},
    {"input": "2", "output": "2"},
    {"input": "3", "output": "3"},

    # --- Reverse order ---
    {"input": "3+3+2+2+1+1", "output": "1+1+2+2+3+3"},
    {"input": "3+2", "output": "2+3"},
    {"input": "3+1", "output": "1+3"},
    {"input": "3+3+3+2+2+1", "output": "1+2+2+3+3+3"},

    # --- Mixed random patterns ---
    {"input": "2+1+3+1+2+3+1", "output": "1+1+1+2+2+3+3"},
    {"input": "3+1+2+3+1+2+3+1", "output": "1+1+1+2+2+3+3+3"},
    {"input": "2+2+3+1+1+3+2+1", "output": "1+1+1+2+2+2+3+3"},
    {"input": "1+3+2+3+2+1+1+3", "output": "1+1+1+2+2+3+3+3"},
    {"input": "2+1+2+1+3+2+3+1", "output": "1+1+1+2+2+2+3+3"},

    # --- Alternating patterns ---
    {"input": "1+3+1+3+1+3", "output": "1+1+1+3+3+3"},
    {"input": "2+1+2+1+2+1", "output": "1+1+1+2+2+2"},
    {"input": "3+1+3+2+3+2", "output": "1+2+2+3+3+3"},
    {"input": "3+2+3+1+3+1", "output": "1+1+2+3+3+3"},

    # --- Only two distinct numbers ---
    {"input": "1+2+1+2+1+2+1+2", "output": "1+1+1+1+2+2+2+2"},
    {"input": "2+3+2+3+2+3", "output": "2+2+2+3+3+3"},
    {"input": "1+3+1+3+1+3", "output": "1+1+1+3+3+3"},

    # --- Skipping one number completely ---
    {"input": "1+1+1+2+2+2", "output": "1+1+1+2+2+2"},
    {"input": "2+2+3+3+3", "output": "2+2+3+3+3"},
    {"input": "1+1+3+3+3", "output": "1+1+3+3+3"},

    # --- Long input (edge near 100 chars) ---
    {"input": "+".join(["3","2","1"] * 17),  # 51 numbers (~100 chars)
     "output": "+".join(["1"]*17 + ["2"]*17 + ["3"]*17)},

    # --- Random longer mixes ---
    {"input": "+".join(["1","3","2","3","1","2"] * 8),
     "output": "+".join(["1"]*16 + ["2"]*16 + ["3"]*16)},
    {"input": "+".join(["3","3","2","1"] * 10),
     "output": "+".join(["1"]*10 + ["2"]*10 + ["3"]*20)},
    {"input": "+".join(["1","2","3"] * 20),
     "output": "+".join(["1"]*20 + ["2"]*20 + ["3"]*20)},
]
