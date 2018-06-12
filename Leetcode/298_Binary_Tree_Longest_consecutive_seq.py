# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def count_consecutive(root):
            if not root:
                maxlen = 0
            else:
                maxlen = 1
                left = count_consecutive(root.left)
                right = count_consecutive(root.right)
                maxlen +=max( left if root.left and root.val+1 == root.left.val else 0 , right if root.right and root.val+1 == root.right.val else 0)
            maxVal[0]=max(maxVal[0],maxlen)
            return maxlen    
    
        maxVal = [0]       
        count_consecutive(root)
        return maxVal[0]
    
    