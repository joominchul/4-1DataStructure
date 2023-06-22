##9.5
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key,end=' ')
        inorder(n.right)
class BSTNode:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
def search_bst(n, key) :
    if n == None :
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
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
def delete_bst_case1 (parent, node, root) :
    if parent is None:
        root = None
    else :
        if parent.left == node :
            parent.left = None
        else :
            parent.right = None

    return root

def delete_bst_case2 (parent, node, root) :
    if node.left is not None :
        child = node.left
    else :
        child = node.right

    if node == root :
        root = child
    else :
        if node is parent.left :
            parent.left = child
        else :
            parent.right = child

    return root

def delete_bst_case3 (parent, node, root) :
    succp = node
    succ = node.right
    while (succ.left != None) :
        succp = succ
        succ = succ.left

    if (succp.left == succ) :
        succp.left = succ.right
    else :
        succp.right = succ.right

    node.key = succ.key
    node.value= succ.value
    return root
def delete_bst (root, key) :
    if root == None : return None

    parent = None
    node = root
    while node != None and node.key != key :
        parent = node
        if key < node.key : node = node.left
        else : node = node.right;

    if node == None :
        return root
    if node.left == None and node.right == None:
        root = delete_bst_case1 (parent, node, root)
    elif node.left==None or node.right==None :
        root = delete_bst_case2 (parent, node, root)
    else :
        root = delete_bst_case3 (parent, node, root)
    return root

class BSTMap():
    def __init__(self):
        self.root=None
    def isEmpty(self):
        return self.root == None
    def search(self,key):
        return search_bst(self.root,key)
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root,n)
    def delete(self, key):
        self.root=delete_bst (self.root, key)

    def display(self, msg = '\n내 전화번호부 :\n---> '):
        print(msg, end='')
        inorder(self.root)
        print()

map = BSTMap()
while True :
    command = input("삽입(i), 탐색(s), 삭제(d), 출력(p), 종료(q): ")
    if command == 'i' :
        name = input("친구의 이름: ")
        phone= input("친구의 전화번호: ")
        map.insert(name,phone)
    elif command == 'd' :
        name = input("친구의 이름: ")
        map.delete(name)
    elif command == 's' :
        name = input("친구의 이름: ")
        node = map.search(name)
        if node is None:
            print("등록되지 않은 친구입니다.")
            continue
        print("친구의 이름: ",node.key)
        print(node.key," 의 전화번호: ",node.value)

    elif command == 'p' :
        map.display()
    elif command == 'q' :
        break