def maxProfit(prices):
    min_price = float('inf')   # best buying price
    max_profit = 0             # maximum profit

    for price in prices:
        if price < min_price:
            min_price = price          # buy at lower price
        else:
            profit = price - min_price # sell today
            max_profit = max(max_profit, profit)

    return max_profit


# Example
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5

