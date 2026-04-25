class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            j = i + 1

            while prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])
                j += 1

                if j == len(prices):
                    break

        return res