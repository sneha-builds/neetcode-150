"""You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1, len(prices)):
                sell=prices[j]
                res=max(res, sell-buy)
        return res
        