# Binary Tree MAximum Path Sum

"""
Given the root of a non-empty bianry trr, return the maximum path sum of any non- empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting
them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the nodes value in the path.

Constraints:
   . 1 <= The number of nodes in the tree <= 1000
   . -1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
        