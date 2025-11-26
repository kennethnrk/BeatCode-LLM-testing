"""
Additional specification-based test cases for problem-8 assertions.

NOTE:
- `assertations.problem-8.assert_problem_8` specifies the behavior for
  `src/problem-7/zephyr_scot.Solve(nums1, nums2, k)`.
- Each case here is a small input intended to exercise different branches
  of the merge logic in `src/problem-7/zephyr_scot.py`.
"""

from __future__ import annotations

from typing import Dict, List


# Each entry is a dict with the exact arguments expected by Solve/asserter.
additional_cases: List[Dict[str, object]] = [
    # --- Trivial / boundary behaviours ---
    # k = 0 → result should be an empty list; loops in the implementation
    # are skipped but the specification must still hold.
    {"nums1": [], "nums2": [], "k": 0},

    # Only nums1 contributes; exercises the secondary loop that drains nums1
    # after the main merge loop finishes.
    {"nums1": [1, 4, 7], "nums2": [], "k": 2},

    # Only nums2 contributes; exercises the secondary loop that drains nums2.
    {"nums1": [], "nums2": [2, 5, 8], "k": 2},

    # Both arrays non-empty, values arranged so that we sometimes pick from
    # nums1 and sometimes from nums2 in the main merge loop.
    {"nums1": [1, 3, 5], "nums2": [2, 4, 6], "k": 4},

    # Equal trailing digits in both arrays; with the specification we must
    # still obtain a lexicographically maximal merged number.
    {"nums1": [6, 6], "nums2": [6, 6], "k": 3},

    # Mixed lengths where k is strictly less than len(nums1) + len(nums2),
    # forcing the specification to reason about the best subsequences rather
    # than simply concatenating everything.
    {"nums1": [3, 9, 1], "nums2": [8, 9], "k": 4},
]


