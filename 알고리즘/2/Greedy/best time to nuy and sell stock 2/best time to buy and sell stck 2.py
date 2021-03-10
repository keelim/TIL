class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]: #저점에서 사서 고점에 판다
                result += prices[i+1]-prices[i]

        return result
