# Kth smallest integer in BST

"""
Given the root of a binary search tree and an integer k, return the kth smallest value(1-indexed) in the tree.

A binary search tree satisfies the following constraints:
. The left subtree of every node contains only nodes with keys less than the nodes key.
. The right subtree of every node contains only nodes with keys greater than the nodes key.
. Both the left and right subtree are also binary search trees.

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if not curr.left:
                k -=1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -=1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1
        