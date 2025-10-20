import math
def Solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit that can be achieved by completing at most two transactions.

    Args:
        prices: A list of integers where prices[i] is the price of a given stock on the i-th day.

    Returns:
        The maximum profit achievable.
    """
    if not prices:
        return 0

    # t1_cost: Minimum price to buy the first stock.
    #          Initialized to positive infinity as we want to minimize this value.
    t1_cost = math.inf
    
    # t1_profit: Maximum profit from the first buy-sell transaction.
    #            Initialized to 0 as no profit has been made yet.
    t1_profit = 0
    
    # t2_cost: Minimum effective cost to buy the second stock.
    #          This accounts for the capital gained from t1_profit.
    #          Initialized to positive infinity.
    t2_cost = math.inf
    
    # t2_profit: Maximum total profit from two buy-sell transactions.
    #            Initialized to 0.
    t2_profit = 0

    for price in prices:
        # Update t1_cost: Find the lowest price to buy the first stock.
        t1_cost = min(t1_cost, price)
        
        # Update t1_profit: Maximize profit for the first transaction.
        # This is (current_price - minimum_buy_price_for_t1).
        t1_profit = max(t1_profit, price - t1_cost)
        
        # Update t2_cost: Find the lowest effective cost to buy the second stock.
        # The effective cost is (current_price - profit_from_first_transaction).
        # We want to minimize this value.
        t2_cost = min(t2_cost, price - t1_profit)
        
        # Update t2_profit: Maximize total profit for two transactions.
        # This is (current_price - minimum_effective_cost_for_t2).
        t2_profit = max(t2_profit, price - t2_cost)
        
    return t2_profit