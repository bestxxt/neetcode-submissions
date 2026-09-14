class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        n = len(prices)
        left = 0
        for right in range(1, n):
            if prices[right] < prices[left]:
                left = right
            else:
                maxp = max(maxp, (prices[right] - prices[left]))

        return maxp