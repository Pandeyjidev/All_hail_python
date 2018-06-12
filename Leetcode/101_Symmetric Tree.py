# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_symmetry(node_l,node_r):
            if node_l and node_r:
                    if node_l.val != node_r.val:
                        return False
                # if node_l.left.val == node_r.right.val and node_l.right.val == node_r.left.val:
                    outter = check_symmetry(node_l.left,node_r.right)
                    inner = check_symmetry(node_l.right,node_r.left)
                    return outter and inner
            elif (node_l and not node_r) or (not node_l and node_r):
                return False
            else:
                return True
        if root is None:
            return True
        if root.left and root.right:
            return check_symmetry(root.left,root.right)
        elif root and (not root.left and not root.right):
            return True
        else:
            return False