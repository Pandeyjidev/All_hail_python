def Search_BinTree(root,key):
    if root: 
        if root.val == key:
            return root
        if root.val > key:
            Search_BinTree(root.left)
        if root.val < key:
            Search_BinTree(root.right)
        