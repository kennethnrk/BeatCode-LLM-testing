test_cases = [
    # Example cases
    {"input": {"nums1": [3,4,6,5], "nums2": [9,1,2,5,8,3], "k": 5}, "output": [9,8,6,5,3]},
    {"input": {"nums1": [6,7], "nums2": [6,0,4], "k": 5}, "output": [6,7,6,0,4]},
    {"input": {"nums1": [3,9], "nums2": [8,9], "k": 3}, "output": [9,8,9]},

    # Edge cases
    {"input": {"nums1": [], "nums2": [1,2,3], "k": 2}, "output": [2,3]},
    {"input": {"nums1": [9,9,9], "nums2": [], "k": 3}, "output": [9,9,9]},
    {"input": {"nums1": [0,0,0], "nums2": [0,0], "k": 4}, "output": [0,0,0,0]},
    {"input": {"nums1": [1], "nums2": [2], "k": 1}, "output": [2]},
    {"input": {"nums1": [1], "nums2": [2], "k": 2}, "output": [2,1]},

    # Both arrays increasing
    {"input": {"nums1": [1,2,3], "nums2": [4,5,6], "k": 4}, "output": [6,5,4,3]},
    
    # Both arrays decreasing
    {"input": {"nums1": [9,8,7], "nums2": [6,5,4], "k": 5}, "output": [9,8,7,6,5]},
    
    # Arrays with equal leading digits
    {"input": {"nums1": [6,6,7], "nums2": [6,7,6], "k": 5}, "output": [7,6,6,7,6]},
    
    # Interleaving digits produce max number
    {"input": {"nums1": [3,4,5,6], "nums2": [9,1,2], "k": 5}, "output": [9,5,6,4,3]},
    
    # Equal digits but one longer
    {"input": {"nums1": [9,9,1], "nums2": [9,1,9], "k": 5}, "output": [9,9,9,1,9]},
    
    # One array has smaller digits but needed for k
    {"input": {"nums1": [1,2], "nums2": [9], "k": 3}, "output": [9,2,1]},
    
    # Single element arrays
    {"input": {"nums1": [5], "nums2": [3], "k": 1}, "output": [5]},
    {"input": {"nums1": [5], "nums2": [3], "k": 2}, "output": [5,3]},

    # Choosing from both where order matters
    {"input": {"nums1": [6,7,5], "nums2": [4,8,1], "k": 4}, "output": [8,7,6,5]},

    # Duplicates and interleaving required
    {"input": {"nums1": [2,5,6,4,4,0], "nums2": [7,3,8,0,6,5,7,6,2], "k": 15}, 
     "output": [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]},

    # Both arrays same digits but different lengths
    {"input": {"nums1": [1,1,1], "nums2": [1,1,1,1], "k": 5}, "output": [1,1,1,1,1]},

    # Large k smaller than total length
    {"input": {"nums1": [9,1,2,5,8,3], "nums2": [3,4,6,5], "k": 5}, "output": [9,8,6,5,3]},
]
