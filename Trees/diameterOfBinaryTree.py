# Diameter of Binary Tree

"""
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:
Input: root = [1,null,2,3,4,5]
Output: 3

Exapmle 2:
Input: root = [1,2,3]
Output: 2
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight),
                           max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]
        