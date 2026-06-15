#Stack : Median Of two sorted array

"""
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.
Your solution must run in O(log(m+n)) time.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedlt = nums1 + nums2
        mergedlt.sort()

        totalLen = len(mergedlt)
        if totalLen %2 ==0:
            return (mergedlt[totalLen //2 -1]+ mergedlt[totalLen//2]) / 2.0
        else:
            return mergedlt[totalLen // 2]

        