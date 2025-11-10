import importlib.util
import os
import pytest

# Base directories
problems_dir = "src"
tests_dir = "tests"

def get_test_cases():
    """Collect all test cases from test files"""
    test_data = []
    
    for i in range(10):
        problem_name = f"problem-{i}"
        test_problem_name = f"problem-{i+1}"
        problem_path = os.path.join(problems_dir, problem_name, "gemini_scot.py")
        test_path = os.path.join(tests_dir, test_problem_name, "test.py")
        
        if not (os.path.exists(problem_path) and os.path.exists(test_path)):
            continue
        
        # Import Solve function
        spec = importlib.util.spec_from_file_location(f"gemini_scot_{i}", problem_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        solve = getattr(module, "Solve")
        
        # Import test_cases
        spec_test = importlib.util.spec_from_file_location(f"test_{i}", test_path)
        test_module = importlib.util.module_from_spec(spec_test)
        spec_test.loader.exec_module(test_module)
        test_cases = getattr(test_module, "test_cases", [])
        
        for j, test_case in enumerate(test_cases):
            test_data.append((problem_name, solve, test_case, j))
    
    return test_data

@pytest.mark.parametrize("problem_name,solve,test_case,test_index", get_test_cases())
def test_gemini_solution(problem_name, solve, test_case, test_index):
    """Test Gemini solutions against test cases"""
    try:
        if isinstance(test_case["input"], dict):
            result = solve(**test_case["input"])
        else:
            result = solve(test_case["input"])
        expected = test_case["output"]
        assert result == expected, (
            f"{problem_name} - Test {test_index + 1}: "
            f"Expected {expected}, got {result}"
        )
    except Exception as e:
        pytest.fail(f"{problem_name} - Test {test_index + 1}: Exception raised: {e}")

