# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def helper(node):
            if node:
                l = helper(node.left)
                r = helper(node.right)
            else:
                return ""
            
            return str(node.val) + "(" + l + ")" + "(" + r + ")"
        
        res = helper(t)
        # print(res)
        res = res.replace("()()","")
        # print(res)
        res = res.replace("()","")
        # print(res)
        return res