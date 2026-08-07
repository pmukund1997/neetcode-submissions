class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        master_high = 0
        for i in range(len(prices)) :
            # creating the window
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    if (prices[j]- prices[i]) > master_high:
                        master_high = prices[j]- prices[i]

        return master_high


