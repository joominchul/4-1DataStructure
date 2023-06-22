class BSTNode:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
def search_max_bst_recur(n) :
    if n != None and n.right != None:
        return search_max_bst_recur(n.right)
    return n

def search_min_bst_recur(n) :
    if n != None and n.left != None:
        return search_min_bst_recur(n.left)
    return n
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')
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

    def isEmpty (self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)

    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def findMax(self): return search_max_bst_recur(self.root)
    def findMin(self): return search_min_bst_recur(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst(self.root, n)


    def display(self, msg = 'BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()
print("\n==========이진탐색트리 테스트==========================")
map=BSTMap()
data=[35,18,7,26,12,3,68,22,30,99]
print("[삽입 연산]: ",data)
for key in data:
    map.insert(key)
map.display("[중위 순회]: ")
print("최댓값=",map.findMax().key)
print("최솟값=",map.findMin().key)