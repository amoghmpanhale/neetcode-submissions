class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 0

        for i in range(len(prices)):
            if prices[i] < prices[low] and i > low:
                low = i
            elif prices[i] > prices[low] and (prices[i] - prices[low]) > profit:
                profit = prices[i] - prices[low]
        
        return profit