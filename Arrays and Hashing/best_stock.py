def maxProfits(prices: list[int]) -> int:
    # use two pointer technique to iterate through the list, and making sure we move from low to high

    buy, sell, maxprofit = 0, 1, 0

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = prices[sell] - prices[buy]
            maxprofit = max(profit, maxprofit)
        else:
            buy = sell
        sell += 1
    return maxprofit


# this solution is optimal and has a runtime of O(n)
print(maxProfits([7,1,5,3,6,4]))