# Last Stone Weight

"""
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Constraints:

 . 1 <= stones.length <= 20
 . 1 <= stones[i] <= 100

"""
  
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
      
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap) 
            x = heapq.heappop(max_heap) 
            
            if y != x:
                heapq.heappush(max_heap, y - x)
                
        return -max_heap[0] if max_heap else 0