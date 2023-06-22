from queueCircular import CircularQueue
class TNode:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')
def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
class BinaryTree:
    def __init__(self,root=None):
        self.root=root
    def isEmpty(self):return self.root==None
    def clear(self):self.root=None
    def printInfix(self,msg='   In-fix : '):
        print(msg,end='')
        inorder(self.root)
        print()
    def printPrefix(self,msg='  Pre-fix : '):
        print(msg, end='')
        preorder(self.root)
        print()
    def printPostfix(self,msg=' Post-fix : '):
        print(msg, end='')
        postorder(self.root)
        print()


b = TNode('B',None,None)
a = TNode('A',None,None)
div=TNode('/',a,b)
c = TNode('C',None,None)
mm =TNode('*',div,c)
d = TNode('D',None,None)
e = TNode('E',None,None)
m = TNode('*', mm, d)
p = TNode('+', m, e)
tree=BinaryTree(p)
tree.printPrefix()
tree.printPostfix()
tree.printInfix()
