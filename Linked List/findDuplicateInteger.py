#Linked List : Find Duplicate Integer

"""
You are given an integer nums containing n + 1 integers. Each integer in nums is in the range 
[1, n] inclusive.
There is exactly one repeated integer in nums and every other integers apears at most once.
Return the repeated integer.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1