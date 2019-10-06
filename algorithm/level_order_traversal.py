"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
	#Write code Here
    if not root:
        return

    res = []
    q = []
    q.append(root)
    while q:
        n = q.pop(0)
        res.append(n.info)
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

    ans = ' '.join('{}'.format(n) for n in res)
    return ans
