# Maximum Product Subarray

"""

Given an integer array nums, find a subarray that has the largest product and return the product.
A subarray is a contiguous non-empty sequence of elements within an array.
You can assume the output will fit into a 32-bit integer.
Note: that the product of an array with a single element is the value of that element.

Constraints:
  . 1<= nums.length <= 1000
  . -10 <= nums[i] <=10
  . The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=nums[0]

        for i in range(len(nums)):
            current=nums[i]
            result=max(result,current)
            for j in range(i+1, len(nums)):
                current *= nums[j]
                result = max(result, current)
        return result
    