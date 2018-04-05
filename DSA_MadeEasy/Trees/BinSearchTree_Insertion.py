class TreeNode():
    def __init__(self,data):
        self.data = data

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root:
        insert(root.left,data)
    if data > root:
        insert(root.right,data) 