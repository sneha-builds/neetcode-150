# Same Binary Tree

"""
Given the roots of two binary trees p and q, return true if the trees are equivalent otherwise return false.
Two binary trees are considered equivalent if they share the exact same structure and the nodes ahve the same value.

Example 1:
Input : p = [1,2,3], q= [1,2,3]
Output : true

Example 2:
Input : p = [4,7], q= [4, null, 7]
Output : false

Example 3:
Input : p = [1,2,3], q= [1,3,2]
Output : false

Constraints:
0 <= The number of nodes in  both trees <=100
-100 <= Node.val <= 100

"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack =[(p,q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True