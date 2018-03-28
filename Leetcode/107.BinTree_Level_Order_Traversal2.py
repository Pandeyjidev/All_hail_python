# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
                
        def BFS(node,c):
            if c in d:
                d[c].append(node.val)
            else:
                d[c] = [node.val]
            if(node.left):
                _ = BFS(node.left,c+1)
            if(node.right):
                _ = BFS(node.right,c+1)
            return d
        if root is None:
            return []
        d = {}
        c = 0
        d = BFS(root, c)
        lst = []
        c = max(d.keys())
        for i in reversed(range(c+1)):
            lst.append(d[i])
        return lst
        
        