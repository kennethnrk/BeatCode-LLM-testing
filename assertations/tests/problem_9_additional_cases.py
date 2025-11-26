"""
Additional specification-based test cases for problem-9 assertions.

NOTE:
- `assertations.problem-9.assert_Solve_correctness` specifies the behavior for
  `src/problem-8/zephyr_scot.Solve(satisfaction)`.
- Each case here is a small satisfaction list chosen to exercise different
  branches in `src/problem-8/zephyr_scot.py` while remaining small enough
  for the exhaustive subset enumeration used in the assertion.
"""

from __future__ import annotations

from typing import List


# Each entry is a satisfaction array that will be passed directly to Solve
# and then checked against the assertion.
additional_cases: List[List[int]] = [
    # All positive values: the greedy algorithm should keep all dishes.
    [1, 2, 3],

    # All non-positive values: the best choice is to cook nothing (result = 0),
    # exercising the early-break path on the first iteration.
    [-3, -2, -1, 0],

    # Mixed positive and negative values where it is optimal to include only
    # a suffix of the sorted array.
    [-1, -8, 0, 5, -9],

    # Another mixed case with both positive and negative values to ensure
    # we exercise multiple loop iterations where the cumulative sum stays
    # positive before we would consider breaking.
    [-2, 5, -1, 3],

    # Case with zeros interleaved with positives.
    [-1, 0, 2, 3],
]


