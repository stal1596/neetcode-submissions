class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, profit = 0, 0
        for right in range(len(prices)):
            profit =  max(prices[right] - prices[left],profit)
            if prices[left] > prices[right]:
                left = right
        return profit

