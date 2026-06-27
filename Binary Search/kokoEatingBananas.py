# Koko Eating Bananas

"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

"""



class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            total_hours = 0
            for pile in piles:
                
                total_hours += (pile + mid - 1) // mid
                
            if total_hours <= h:
                ans = mid      
                high = mid - 1 
            else:
                low = mid + 1   
                
        return ans