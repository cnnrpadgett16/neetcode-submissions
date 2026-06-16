class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        answer = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                answer = max(answer, profit)
        return answer