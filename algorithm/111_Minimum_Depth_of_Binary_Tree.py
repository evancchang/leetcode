# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        if (not root.left) and (not root.right):
            return 1
        
        left_level = self.minDepth(root.left)
        right_level = self.minDepth(root.right)
        
        if not root.left: 
            return 1 + right_level
        if not root.right:
            return 1 + left_level        
        
        return 1 + min(left_level, right_level)
