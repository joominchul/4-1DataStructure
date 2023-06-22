class BSTNode:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key,end=' ')
        inorder(n.right)
def insert_bst(r, n) :
    if n.key < r.key:
        if r.left is None :
           r.left = n
           return True
        else :
           return insert_bst(r.left, n)
    elif n.key > r.key :
        if r.right is None :
           r.right = n
           return True
        else :
           return insert_bst(r.right, n)
    else :
        return False
class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty(self):
        return self.root == None
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root,n)
    def display(self, msg='BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

map = BSTMap()
data = [11,3,4,1,56,5,6,2,98,32,32]
print("[삽입 연산] : ", data)
for key in data :
    map.insert(key)
map.display("[정렬 결과] : ")
