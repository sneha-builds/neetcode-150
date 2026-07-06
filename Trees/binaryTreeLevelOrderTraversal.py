# Binary Tree Level Order Traversal

"""

Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the 
values of nodes at a particular level in tree, from left to right.

Constraints:
0 <= the number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000

"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            current_level = []
            next_level_queue = []
            
            for node in queue:
                current_level.append(node.val)
                
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            
            result.append(current_level)
            queue = next_level_queue
            
        return result