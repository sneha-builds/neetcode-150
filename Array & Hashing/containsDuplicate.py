"""Problem:Given an integer array nums, return true if any value appears more than once in 
 the array, otherwise return false."""
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
