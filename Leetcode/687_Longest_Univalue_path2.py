# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def runner(root,res):
            l,r=0,0
            if root.left:
                l = runner(root.left,res)
                l = l+1 if root.left.val == root.val else 0
            if root.right:
                r = runner(root.right,res)
                r = r+1 if root.right.val == root.val else 0
            res[0] = max(res[0],l+r)
            return max(l,r)
        if not root:
            return 0
        res = [0]
        runner(root,res)
        return res[0]
    
    