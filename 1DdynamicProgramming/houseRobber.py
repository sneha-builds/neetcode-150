# House Robber

"""

You are given an integer array nums where nums and nums[i] represents the amount of money the ith house has.
The house are arranged in s straight line, i.e, the house is the neighbour of the (i-1)th and (i+1)th house.

You are planning to rob money, but you cannpt rob two adjacent houses because the security system will automatically alert
the police if two adjacent houses were both broken into.

Return the maximum amount of money ypu can rob without alerting the police.

Constraints:
  . 1 <= nums.length <=100
  . <= nums[i] <= 100

"""

class Solution:
    def rob(self, nums:List[int]) -> int:
        rob1, rob2 = 0,0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2