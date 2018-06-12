# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def BFS(node,c):
            if c in d:
                d[c].append(node.val)
            else:
                d[c] = [node.val]
            if node.left:
                _ = BFS(node.left,c+1)
            if node.right:
                _ = BFS(node.right,c+1)
            return d
        
        def addlist(lst):
            return sum(lst),len(lst)
        
        if root is None:
            return []
        d = {}
        c = 0
        d = BFS(root,c)
        lst = []
        c = max(d.keys())
        res = []
        print(d)
        for i in range(c+1):
            summation, divisor = addlist(d[i])
            res.append(float(summation)/float(divisor))
        return res
            
