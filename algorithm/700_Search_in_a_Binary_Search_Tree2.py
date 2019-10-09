# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        q = [root]
        while q:
            curr = q.pop(0)
            if curr.val == val:
                return curr
            elif curr.val < val:
                if curr.right:
                    q.append(curr.right)
            else:
                if curr.left:
                    q.append(curr.left)
                
        return None
        
        
