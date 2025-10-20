def Solve(prices):
    max_profit = 0
    profit1 = 0
    profit2 = 0
    min_price = prices[0]

    for I in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        profit1 = max(profit1, prices[i] - min_price)

    for j in range(1, len(prices)):
        for k in range(j+2, len(prices)):
            min_price = min(prices[j:k+1], key=lambda x: x[0])[1]
            profit2 = max(profit2, prices[k] - min_price)

        max_profit = max(max_profit, profit1 + profit2)

    return max_profit
