# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from queue import *
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = [root]
        res = [[root.val]]
        
        while q:
            temp_q = []
            for node in q:
                if node.left:
                    temp_q.append(node.left)
                if(node.right):
                    temp_q.append(node.right)
            if temp_q:
                res.append([ node.val for node in temp_q])
            q = temp_q
        return res