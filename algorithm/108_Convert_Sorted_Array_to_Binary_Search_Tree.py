# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(nums[0])
        
        root = TreeNode(nums[l//2])
        root.left = self.sortedArrayToBST(nums[:l//2])
        root.right = self.sortedArrayToBST(nums[l//2 + 1:])
        
        return root
        
