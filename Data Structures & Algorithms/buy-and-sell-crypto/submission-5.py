class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        answer = 0
        profit = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                answer = max(profit, answer)
        return answer
