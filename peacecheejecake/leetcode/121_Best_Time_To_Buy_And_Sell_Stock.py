# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = [0] * len(prices)
        max_profit = 0
        for i in range(len(prices) - 2, -1, -1):
            max_after = max(max_prices[i + 1], prices[i + 1])
            max_prices[i] = max_after
            max_profit = max(max_profit, max_after - prices[i])
        return max_profit
        