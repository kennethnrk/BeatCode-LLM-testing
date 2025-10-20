import importlib.util
import os

# Base directories
problems_dir = "src"
tests_dir = "tests"

for i in range(10):
    problem_name = f"problem-{i}"
    test_problem_name = f"problem-{i+1}"
    problem_path = os.path.join(problems_dir, problem_name, "gemini_scot.py")
    test_path = os.path.join(tests_dir, test_problem_name, "test.py")

    # Skip if files are missing
    print(problem_path, test_path)
    if not (os.path.exists(problem_path) and os.path.exists(test_path)):
        print(f"Skipping {problem_name}: missing gemini_scot.py or test.py")
        continue

    # Dynamically import solve() from gemini_scot.py
    spec = importlib.util.spec_from_file_location(f"gemini_scot.py", problem_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solve = getattr(module, "Solve")

    # Import test_cases from test.py
    spec_test = importlib.util.spec_from_file_location(f"test_{i}", test_path)
    test_module = importlib.util.module_from_spec(spec_test)
    spec_test.loader.exec_module(test_module)
    test_cases = getattr(test_module, "test_cases", [])

    pass_counter = 0
    fail_counter = 0
    for j, test in enumerate(test_cases):

        try:
            result = (
                solve(**test["input"])
                if isinstance(test["input"], (dict))
                else solve(test["input"])
            )
            expected = test["output"]
            if result == expected:
                pass_counter += 1
                # print(f"Test {j+1}:  Passed")
            else:
                fail_counter += 1
                # print(f"Test {j+1}:  Failed - Expected: {expected}, Got: {result}\n")
        except Exception as e:
            fail_counter += 1

    print(f"\n=== Summary for {problem_name} ===")
    print(
        f"Passed: {pass_counter}, Failed: {fail_counter}, percentage: {pass_counter / (pass_counter + fail_counter) * 100 if (pass_counter + fail_counter) > 0 else 0:.2f}%"
    )
