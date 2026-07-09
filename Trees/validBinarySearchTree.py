# Valid Binary Search Tree

"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary serach tree satisfies the following constraints:
. The left subtree of every node contains only nodes with keys less than the node's key.
. The right subtree of every node contains only nodes with keys greater than the node's key.
. Both the left and right subtree are also binary search trees.

Constraints:
. 1 <= the number of nodes in the tree <= 100.
. -1000 <= Node.val <= 1000

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

        