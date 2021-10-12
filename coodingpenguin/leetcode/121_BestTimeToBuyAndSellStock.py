# 문제: 121. Best Time to Buy and Sell Stock
# 링크: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


#  시간/공간: 948ms / 25MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]  # 최소 가격
        max_profit = 0  # 최대 이윤
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i - 1])  # 최소 가격 갱신
            profit = prices[i] - min_price  # 새로운 이윤
            # 최대 이윤보다 크다면
            if max_profit < profit:
                max_profit = profit  # 갱신
        return max_profit
