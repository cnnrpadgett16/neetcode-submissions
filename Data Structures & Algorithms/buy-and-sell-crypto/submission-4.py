class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        answer = 0
        profit = 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            else:
                answer = max(profit, answer)
        return answer
