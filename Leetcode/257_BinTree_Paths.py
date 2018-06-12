# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def compute_paths(self, root, L, path=""):
            print(L)
            print(path)
            
            if root==None:
                return []
            
            elif root.left==None and root.right==None:
                path = path+"->"+str(root.val)
                print("\n")
                print(L)
                L.append(path[2:])
                print(L)
                print("\n")
            
            if root.left!=None: 
                self.compute_paths(root.left, L, path=path+"->"+str(root.val))
            if root.right!=None: 
                self.compute_paths(root.right, L, path=path+"->"+str(root.val))
            #return L
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        L = []
        self.compute_paths(root, L, path="")
        return L