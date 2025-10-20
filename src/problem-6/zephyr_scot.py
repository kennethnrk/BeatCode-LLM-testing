def Solve(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    # Sort projects based on profit-to-capital ratio
    projects = list(zip(profits, capital))
    projects.sort(key=lambda x: x[1] / x[0])

    # Initialize variables
    total_capital = w
    num_projects = 0

    # Iterate through projects, choosing the best ones based on remaining capital
    for profit, capital_req in projects:
        if capital_req <= total_capital:
            total_capital += profit
            num_projects += 1
            if num_projects == k:
                # Reached maximum number of projects, find the best remaining one
                for remaining_profit, remaining_capital in projects[num_projects:]:
                    if remaining_profit / remaining_capital > profit / capital_req:
                        total_capital += remaining_profit
                        num_projects += 1
                        break
        elif num_projects < k:
            continue

    # Return final maximized capital
    return total_capital
