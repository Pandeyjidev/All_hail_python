# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inOrder(node):
            if node is not None:
                inOrder(node.left)
                lst.append(node)
                inOrder(node.right)

        lst = []
        inOrder(root)
        
        n = len(lst)
        for i in range(n-2, -1, -1):
            # print(i)
            # print(lst[i].val)
            # print(lst[i+1].val)
            lst[i].val += lst[i+1].val
            # print("\n")
        return root