# 1 D Dynamic Programming : Climbing Stairs
"""You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
               
        ways_to_n_minus_2 = 1
        ways_to_n_minus_1 = 2
        
        for i in range(3, n + 1):
            current_ways = ways_to_n_minus_1 + ways_to_n_minus_2
            
            ways_to_n_minus_2 = ways_to_n_minus_1
            ways_to_n_minus_1 = current_ways
            
        return ways_to_n_minus_1