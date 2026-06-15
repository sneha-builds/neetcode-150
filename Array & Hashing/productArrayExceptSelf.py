#Array and Hashing: Product Array Except Self

"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]

            result[i] = product
        return result