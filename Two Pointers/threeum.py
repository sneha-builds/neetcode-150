#Two Pointers : Three Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[List[int]]]:
        res = set()
        dups = set()
        
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                seen = set()
                
                for j in range(i + 1, len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in seen:
                        res.add(tuple(sorted((nums[i], nums[j], complement))))
                    seen.add(nums[j])
                    
        return [list(triplet) for triplet in res]