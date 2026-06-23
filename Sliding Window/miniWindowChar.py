#Minimum Window Substring

"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        dict_t = Counter(t)
        required_unique_chars = len(dict_t)
        
        window_counts = {}
        
        formed = 0
        
        ans = float("inf"), None, None
        
        start = 0  
        
        
        for end in range(len(s)):
            character = s[end]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
                
            
            while start <= end and formed == required_unique_chars:
                character = s[start]
                
                
                current_window_len = end - start + 1
                if current_window_len < ans[0]:
                    ans = (current_window_len, start, end)
                    
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                    
                
                start += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]