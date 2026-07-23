# Coin Change

"""

You are given an integer array coins representing coins of different denominations(e.g. 1 dollar, 5 dollar, etc)
and an integer amount representing a target amount of money.

Return the fewest numbe rof coins that you need to make up the exact target amount. If it is impossible to make up
the amount, return -1.

You may assume that you have an unlimited number of each coin.

Constraints:
  . 1<= coins.length <= 10
  . 1 <= coins[i] <= 2^31 -1
  . 0 <= amount <= 10000

"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        return dp[amount] if dp[amount] != amount +1 else-1