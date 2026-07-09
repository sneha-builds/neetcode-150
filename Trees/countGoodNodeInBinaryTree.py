# Count Good Nodes In Binary Tree

"""

Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value
greater than the value of node x.
Given the root of a binary tree root, return the number of good nodes within the tree.

Constraints:
1 <= number of nodes in the tree <=100
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, -float('inf')))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            if node.left:
                q.append((node.left, max(maxval, node.val)))

            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res
        