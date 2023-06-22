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
    def printInOrder(self,msg='   In-Order : '):
        print(msg,end='')
        inorder(self.root)
        print()
    def printPreOrder(self,msg='  Pre-Order : '):
        print(msg, end='')
        preorder(self.root)
        print()
    def printPostOrder(self,msg=' Post-Order : '):
        print(msg, end='')
        postorder(self.root)
        print()
    def printLevelOrder(self,msg='Level-Order : '):
        print(msg, end='')
        levelorder(self.root)
        print()
d = TNode('D', None, None)
f = TNode('F', None, None)
g = TNode('G', None, None)
h = TNode('H', None, None)
b = TNode('B', d, None)
e = TNode('E', g, h)
c = TNode('C', e, f)
a = TNode('A', b, c)
tree=BinaryTree(a)
tree.printInOrder()
tree.printPreOrder()
tree.printPostOrder()
tree.printLevelOrder()
