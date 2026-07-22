class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0
        for price in prices:
            if price < cheapest:
                cheapest = price
            today_profit = price - cheapest
            if today_profit > max_profit:
                max_profit = today_profit
        return max_profit
