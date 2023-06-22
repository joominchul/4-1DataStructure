from linkedList import LinkedList
class Term:
    def __init__(self,coef,expo):
        self.expo=int(expo)
        self.coef=coef
class Node:
    def __init__ (self, elem, link=None):
        x,y=elem
        self.data = Term(x,y)
        self.link = link
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()
    def degree(self):
        node=self.head
        return node.data.expo
    def display(self, msg=" 입력 다항식: "):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data.coef," x^",node.data.expo,"+ ",end='')
            node = node.link
        print()
    def read(self):
        self.clear()
        pos=0
        while True:
            elem=list(map(float,input("계수 차수 입력(종료:-1): ").split()))
            if elem[0]==-1 and elem[1]==-1:
                break
            self.insert(pos,elem)
            pos+=1
    def add(self,B):
        C=SparsePoly()
        a=self.head
        b=B.head
        pos=0
        elem = [0,0]
        while a!=None or b!=None:
            if a==None or (b!=None and a.data.expo < b.data.expo):
                elem[0] = b.data.coef
                elem[1] = b.data.expo
                C.insert(pos, elem)
                pos += 1
                b = b.link
            elif b==None or (a!=None and b.data.expo < a.data.expo):
                elem[0] = a.data.coef
                elem[1] = a.data.expo
                C.insert(pos, elem)
                pos += 1
                a = a.link
            else:
                elem[0]=a.data.coef+b.data.coef
                elem[1]=a.data.expo
                C.insert(pos,elem)
                pos+=1
                a=a.link
                b=b.link
        return C
a=SparsePoly()
a.read()
a.display()
b=SparsePoly()
b.read()
b.display()
a.display("A = ")
b.display("B = ")
c=a.add(b)
c.display("A+B=")
