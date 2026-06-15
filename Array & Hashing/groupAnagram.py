#Array and Hashing: Group Anagram

"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s)
        return list(result.values())