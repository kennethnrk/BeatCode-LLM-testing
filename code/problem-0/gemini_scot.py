def Solve(s: str) -> str:
    """
    Rearranges the summands in a given sum string (containing 1s, 2s, and 3s)
    so that they appear in non-decreasing order.

    Args:
        s: A non-empty string representing a sum (e.g., "3+2+1").
           Contains only digits '1', '2', '3' and '+' characters.

    Returns:
        A new string with summands in non-decreasing order (e.g., "1+2+3").
    """
    # Step 1 & 2: Parse the input string, extract numbers, and convert to integers.
    # The split() method handles both cases: "1+2+3" -> ['1', '2', '3']
    # and "2" -> ['2'] correctly.
    numbers = [int(num_str) for num_str in s.split('+')]

    # Step 3: Sort the numbers in non-decreasing order.
    numbers.sort()

    # Step 4 & 5: Convert sorted integers back to strings and reconstruct the sum string.
    # Use a list comprehension to convert each integer to a string,
    # then join them with '+' characters.
    sorted_sum_parts = [str(num) for num in numbers]
    result_sum = "+".join(sorted_sum_parts)

    # Step 6: Return the result.
    return result_sum

