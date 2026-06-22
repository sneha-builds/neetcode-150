# Permutation in String

"""
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1 or false otherwise. That means if a permutation of s1 exists as a
substring of s2, then return true.
Both strings only contain lowercase letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        if s1_count == s2_count:
            return True
            
        for i in range(len1, len2):
            
            s2_count[ord(s2[i]) - ord('a')] += 1
            
            s2_count[ord(s2[i - len1]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
                
        return False

        