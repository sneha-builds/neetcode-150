# Kth Largest Element in an Array

"""

Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Constraints:

  . 1 <= k <= nums.length <= 10000
  . -1000 <= nums[i] <= 1000

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
        
