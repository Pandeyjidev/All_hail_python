# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preOrder(node):
            if node:
                lst.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
            else:
                return
        
        lst = []
        preOrder(root)
        lst = sorted(set(lst))
        print(lst)
        
        if(len(lst)>1):
            return lst[1]
        else:
            return -1
        