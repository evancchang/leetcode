# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        q = deque()
        q.append(root)
        while q:
            depth += 1
            for _ in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.popleft()
            
        return depth

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # bottom-up
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
