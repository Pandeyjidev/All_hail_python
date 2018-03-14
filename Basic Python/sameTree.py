def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    flag=1
    def deal(node1,node2):
        if node1 and node2:
            if node1.val!=node2.val:
                nonlocal flag
                flag=0
            else:
                deal(node1.left,node2.left)
                deal(node1.right,node2.right)
        elif not node1 and not node2:
            pass
        else:
            flag=0
    deal(p,q)
    
    if flag==1:return True
    else:return False