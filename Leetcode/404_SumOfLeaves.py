# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sumLeft(node):
            if node:
                if node.left and node.left.left == None and node.left.right == None:
                    summation[0] += node.left.val
                sumLeft(node.left)
                sumLeft(node.right)
                
            else:
                return
        summation = [0]
        sumLeft(root)
        return summation[0]