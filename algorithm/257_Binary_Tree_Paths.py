# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
            
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
            
        for path in self.binaryTreePaths(root.left):
            res.append(str(root.val)+'->'+path)
        for path in self.binaryTreePaths(root.right):
            res.append(str(root.val)+'->'+path)
            
        return res
