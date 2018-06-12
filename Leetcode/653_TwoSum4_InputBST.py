# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def makeList(node):
            if node: 
                lst.append(node.val)
                makeList(node.left)
                makeList(node.right)
            else:
                return
        lst = []
        makeList(root)
        if len(lst) <=1:
            return False
        print(lst)
        sorted(lst)
        for i,num in enumerate(lst):
            if (k-num) in lst and num is not 'null':
                if num == (k-num):
                    if i+1 < len(lst):
                        if (lst[i-1]==num or lst[i+1]==num):
                            return True
                else:
                    return True
        return False