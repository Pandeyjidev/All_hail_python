# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def calculate(node):
            if node is not None:
                left , right = calculate(node.left) , calculate(node.right)
                self.res += abs(left-right)
                return left + right + node.val
            else:
                return 0
            
        calculate(root)
        return self.res
            