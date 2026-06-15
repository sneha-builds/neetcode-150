#Two Pointers : Container with most water

"""
You are given an integer array heights where heights[i] represents the height of the i(th) bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res =0
        l, r =0, len(heights) -1

        while l<r:
            area = (r-l) * min (heights[l], heights[r])
            res = max(res, area)
        
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
        return res