import queue
class TreeNode():
    def __init__(self,val, leftChild = None, rightChild = None):
        self.data = val
        self.left = leftChild
        self.right = rightChild

class Tree():
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self,val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(val,self.root)
    def _add(self,val,node):
        if (val<node.data):
            if(node.left is not None):
                self._add(val,node.left)
            else:
                node.left = TreeNode(val)
        else:
            if(node.right is not None):
                self._add(val,node.right)
            else:
                node.right = TreeNode(val)
    def preOrder(self,subTree):
        if (subTree is not None):
            print(subTree.data)
            self.preOrder(subTree.left)
            self.preOrder(subTree.right)

    def inOrder(self,subTree):
        if(subTree is not None):
            self.inOrder(subTree.left)
            print(subTree.data)
            self.inOrder(subTree.right)

    def postOrder(self,subTree):
        if(subTree is not None):
            self.postOrder(subTree.left)
            self.postOrder(subTree.right)
            print(subTree.data)
    def BreadthFirstSearch(self,binTree):
        q = queue.Queue()
        q.put(binTree)

        while(not q.empty()):
            node = q.get()
            print(node.data)

            if(node.left is not None):
                q.put(node.left)
            if(node.right is not None):
                q.put(node.right)
            

T = Tree()
T.add(3)
T.add(5)
T.add(1)
T.add(0)
T.add(21)
T.add(2)
T.add(100)

T.preOrder(T.getRoot())
print("\n")
T.postOrder(T.getRoot())
print("\n")
T.inOrder(T.getRoot())
print("\n")
T.BreadthFirstSearch(T.getRoot())
