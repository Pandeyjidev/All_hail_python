# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inOrder(node):
            if node:
                inOrder(node.left)
                lst.append(node.val)
                inOrder(node.right)
            else:
                return
        lst = []
        inOrder(root)
        print(lst)
        
        lst = sorted(set(lst))
        print(lst)
        return lst[k-1]