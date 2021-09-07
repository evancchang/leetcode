# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return ret

class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def preorder(root):
            if not root:
                return
            ret.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)        
        return ret    
