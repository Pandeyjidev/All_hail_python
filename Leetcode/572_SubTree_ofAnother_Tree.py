# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traverse(s,t)
    
    def subTree(self, x, y):
        if not x and not y:
            return True
        if (not x and y) or (x and not y):
            return False
        return (x.val == y.val) and self.subTree(x.left,y.left) and self.subTree(x.right,y.right)

        
    def traverse(self, s, t):
        o = (s and (self.subTree(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t)))
        if not o:
            return False
        else:
            return True
