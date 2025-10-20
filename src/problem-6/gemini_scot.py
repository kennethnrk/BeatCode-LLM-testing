import heapq

def Solve(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    # 1. Combine profits and capital into a list of projects.
    # Each project is stored as a tuple: (capital_required, pure_profit).
    n = len(profits)
    projects = []
    for i in range(n):
        projects.append((capital[i], profits[i]))

    # 2. Sort all projects based on their capital requirements in ascending order.
    # This makes it efficient to find projects that become affordable as 'w' increases.
    projects.sort()

    # max_heap will store the profits of projects that are currently affordable.
    # We use Python's heapq (a min-heap) by storing negative profits to simulate a max-heap.
    affordable_profits_max_heap = []

    # project_idx is a pointer to the next project in the sorted 'projects' list
    # that we haven't yet considered adding to the heap.
    project_idx = 0

    # 3. Iterate k times (to complete at most k projects).
    for _ in range(k):
        # a. Add all projects that can be afforded with the current capital 'w'
        # to the max-heap.
        # We iterate through 'projects' list as long as there are projects left
        # and their capital requirement is less than or equal to our current 'w'.
        while project_idx < n and projects[project_idx][0] <= w:
            # Push the profit (negated to simulate max-heap) into the heap.
            heapq.heappush(affordable_profits_max_heap, -projects[project_idx][1])
            project_idx += 1

        # b. If the max-heap is empty, it means we cannot afford any more projects
        # with our current capital 'w'. Since our capital can only increase,
        # we won't be able to afford new projects in subsequent iterations either.
        # So, we stop early.
        if not affordable_profits_max_heap:
            break

        # c. Otherwise, extract the maximum profit from the heap. This represents
        # completing the most profitable project we can currently afford.
        current_max_profit = -heapq.heappop(affordable_profits_max_heap)
        
        # Add this profit to our current total capital.
        w += current_max_profit

    # 4. After completing at most k projects (or stopping early),
    # 'w' holds the maximized final capital.
    return w