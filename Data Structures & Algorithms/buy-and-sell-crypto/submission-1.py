class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
    
        while r < len(prices):
            if prices[r] > prices[l]:
                p = prices[r] - prices[l]
                if p > res:
                    res = p
            else:
                l = r
            r += 1
        return res

