"""You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise."""


class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
                    
        stack = [None] * len(s)
        top = -1          
        
        match = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            
            if char in match:
                
                if top < 0 or stack[top] != match[char]:
                    return False
                top -= 1  
            else:
                
                top += 1 
                stack[top] = char 
                
        
        return top == -1