# Invert Binary Tree

"""
You are given the root of a binary tree root. Invert the binary tree and return its root.

Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Input: root = [3,2,1]
Output: [3,1,2]

Input: root = []
Output: []

Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root     