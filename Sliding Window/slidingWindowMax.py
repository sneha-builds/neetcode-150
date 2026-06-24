# Sliding Window Maximum

"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at 
the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.
return a list that contains element the maximum element in the window at each step.
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
        
        result = []
        
        q = deque()  
        
        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
                
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            q.append(i)
            
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result