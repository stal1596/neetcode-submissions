class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p, left = 0, 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            max_p = max(max_p,profit)
            if prices[right] < prices[left]:
                left = right
        return max_p