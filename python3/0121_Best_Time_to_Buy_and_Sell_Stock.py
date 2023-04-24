class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minPrice, profit = prices[0], 0
        for i in range(len(prices)):
            profit = max(prices[i] - minPrice, profit)
            minPrice = min(minPrice, prices[i])
        return profit
