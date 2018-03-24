class ExpressionTree():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isOperator(c):
    if(c=='+' or c=='-' or c=='*' or c=='/' or c=='%'):
        return True
    else:
        return False

def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.val)
        inorder(t.right)


def constructTree(postfix):
    stack = []
    for c in postfix:
        if not isOperator(c):
            t=ExpressionTree(c)
            stack.append(t)
        else:
            t = ExpressionTree(c)
            t1 = stack.pop()
            t2 = stack.pop()

            t.right = t1
            t.left = t2

            stack.append(t)
    res=stack.pop()

    return res


exp = "ab+ef*g*-"
r = constructTree(exp)
print("Infix expression is : ")
inorder(r)