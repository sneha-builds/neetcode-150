#Sliding Window : Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
                
            char_set.add(s[end])
            
            current_length = end - start + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length
    