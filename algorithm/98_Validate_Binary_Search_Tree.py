from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        
        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            root, lower, upper = q.popleft()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            q.append((root.left, lower, val))
            q.append((root.right, val, upper))
            
        return True
        
