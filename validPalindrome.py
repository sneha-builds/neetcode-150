"""Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9)."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new= ''
        for i in s:
            if i.isalnum():
                new+= i.lower()
        return new == new[::-1]