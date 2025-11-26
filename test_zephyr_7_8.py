import importlib.util
import os
from typing import Any, Dict, List, Tuple

import pytest

# Base directories
problems_dir = "src"
tests_dir = "tests"


def load_solve(problem_index: int):
    """Dynamically import Solve for the given problem index."""
    problem_name = f"problem-{problem_index}"
    problem_path = os.path.join(problems_dir, problem_name, "zephyr_scot.py")

    if not os.path.exists(problem_path):
        raise FileNotFoundError(f"Could not find problem implementation at {problem_path}")

    spec = importlib.util.spec_from_file_location(f"zephyr_scot_{problem_index}", problem_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return getattr(module, "Solve")


def get_original_test_cases() -> List[Tuple[str, Any, Dict[str, Any], int]]:
    """
    Collect the *original* test cases for problems 7 and 8.

    NOTE:
    - For historical reasons, problem-7 uses tests from tests/problem-8,
      and problem-8 uses tests from tests/problem-9 (matching test_zephyr.py).
    """
    mappings = {
        7: 8,  # src/problem-7  <->  tests/problem-8
        8: 9,  # src/problem-8  <->  tests/problem-9
    }

    test_data: List[Tuple[str, Any, Dict[str, Any], int]] = []

    for problem_index, test_problem_index in mappings.items():
        problem_name = f"problem-{problem_index}"
        problem_path = os.path.join(problems_dir, problem_name, "zephyr_scot.py")
        test_path = os.path.join(tests_dir, f"problem-{test_problem_index}", "test.py")

        if not (os.path.exists(problem_path) and os.path.exists(test_path)):
            continue

        # Import Solve function
        spec = importlib.util.spec_from_file_location(f"zephyr_scot_{problem_index}", problem_path)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        solve = getattr(module, "Solve")

        # Import test_cases list from the corresponding tests/problem-*/test.py
        spec_test = importlib.util.spec_from_file_location(f"test_{problem_index}", test_path)
        test_module = importlib.util.module_from_spec(spec_test)
        assert spec_test.loader is not None
        spec_test.loader.exec_module(test_module)
        test_cases = getattr(test_module, "test_cases", [])

        for j, test_case in enumerate(test_cases):
            test_data.append((problem_name, solve, test_case, j))

    return test_data


def get_assertation_based_cases():
    """
    Build test inputs that will be validated using the formal specifications
    in `assertations/problem-8.py` and `assertations/problem-9.py`.

    - assertations.problem-8  ->  src/problem-7 (Create Maximum Number)
    - assertations.problem-9  ->  src/problem-8 (Like-time Coefficient)
    """
    # Load the formal specification functions from the assertations directory.
    # These files use hyphenated names (problem-8.py, problem-9.py), so we use
    # importlib instead of normal Python imports.
    assertations_dir = "assertations"

    def _load_asserter(filename: str, func_name: str):
        path = os.path.join(assertations_dir, filename)
        spec = importlib.util.spec_from_file_location(func_name, path)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        return getattr(module, func_name)

    assert_problem_8 = _load_asserter("problem-8.py", "assert_problem_8")
    assert_Solve_correctness = _load_asserter("problem-9.py", "assert_Solve_correctness")

    from assertations.tests.problem_8_additional_cases import (  # type: ignore
        additional_cases as p8_cases,
    )
    from assertations.tests.problem_9_additional_cases import (  # type: ignore
        additional_cases as p9_cases,
    )

    solve_p7 = load_solve(7)
    solve_p8 = load_solve(8)

    data = []

    # Problem-7 (Create Maximum Number) with assertion from problem-8
    for idx, case in enumerate(p8_cases):
        data.append(
            (
                "problem-7",
                solve_p7,
                "p8",
                idx,
                case,
                assert_problem_8,
            )
        )

    # Problem-8 (Like-time Coefficient) with assertion from problem-9
    for idx, satisfaction in enumerate(p9_cases):
        data.append(
            (
                "problem-8",
                solve_p8,
                "p9",
                idx,
                satisfaction,
                assert_Solve_correctness,
            )
        )

    return data


@pytest.mark.parametrize("problem_name,solve,test_case,test_index", get_original_test_cases())
def test_zephyr_original_7_8(problem_name, solve, test_case, test_index):
    """Run the original example/edge-case tests for problems 7 and 8."""
    try:
        if isinstance(test_case["input"], dict):
            result = solve(**test_case["input"])
        else:
            result = solve(test_case["input"])
        expected = test_case["output"]
        assert result == expected, (
            f"{problem_name} - Original Test {test_index + 1}: "
            f"Expected {expected}, got {result}"
        )
    except Exception as e:
        pytest.fail(f"{problem_name} - Original Test {test_index + 1}: Exception raised: {e}")


@pytest.mark.parametrize(
    "problem_name,solve,kind,case_index,case,asserter",
    get_assertation_based_cases(),
)
def test_zephyr_assertations_7_8(problem_name, solve, kind, case_index, case, asserter):
    """
    Run specification-based tests for problems 7 and 8 using the formal
    assertation functions.
    """
    try:
        if kind == "p8":
            # case is a dict with keys: nums1, nums2, k
            nums1 = case["nums1"]
            nums2 = case["nums2"]
            k = case["k"]
            result = solve(nums1, nums2, k)
            asserter(result, nums1, nums2, k)
        else:
            # kind == "p9": case is a satisfaction list
            satisfaction = case
            result = solve(satisfaction)
            asserter(satisfaction, result)
    except AssertionError:
        # Let assertion failures surface as regular pytest assertion failures
        raise
    except Exception as e:
        pytest.fail(
            f"{problem_name} - Assertation-based Test {case_index + 1} "
            f"(kind={kind}): Exception raised: {e}"
        )


