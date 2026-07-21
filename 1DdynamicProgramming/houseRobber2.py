#  House Robber II

"""

You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The house are arranged in circle, i.e, the first house and the last house are neighbours.

You are planning to rob money from the bouses, but you cannot rob two adjacent houses because the 
security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Constraints:
  . 1 <= nums.length <=100
  . 0 < nums[i] <= 200

"""

class Solution:
    def rob(self, nums:list[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1, rob2 = 0,0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2