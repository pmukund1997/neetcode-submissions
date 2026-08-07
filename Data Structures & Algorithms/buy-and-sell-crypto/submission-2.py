class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best_profit = 0
        for item in prices:
            if item < min_price:
                min_price = item
            current_profit = item - min_price
            if current_profit > best_profit:
                best_profit = current_profit

        return best_profit