class ArrayList:
    def __init__(self):
        self.items=[]
    def append(self, elem):
        self.items.append(elem)
    def getEntry(self,pos):
        return self.items[pos]
    def insert(self, pos, elem):
        l = list()
        for i in range(pos):
            l.append(self.getEntry(i))
        l.append(elem)
        for i in range(pos, self.size()):
            l.append(self.getEntry(i))
        self.items=l
    def size(self):
        return len(self.items)
    def display(self, msg='ArrayList:'):
        print(msg, '항목수=',self.size(), self.items)
    #3.12
    def delete(self,pos):
        l=list()
        for i in range(pos+1):
            l.append(self.getEntry(i))
        l.pop(-1)
        for i in range(pos+1,self.size()):
            l.append(self.getEntry(i))
        self.items=l
    #3
    def find(self,item):
        for i in self.items:
            if item==i:
                return True
        return False
    #4
    def merge(self,list):
        for i in list:
            self.append(i)
        return self
    def merge1(self,list):
        n=0
        for i in list:
            for j in self.items:
                if i==j:
                    n=1
            if n==0:
                self.append(i)
        return self
l=ArrayList()
l.display('파이썬 리스트로 구현한 리스트 테스트')
l.insert(0,10)
l.insert(0,20)
l.insert(1,30)
l.insert(l.size(),40)
l.insert(2,50)
l.display('파이썬 리스트로 구현한 리스트 테스트')
#3.12
l.delete(4)
l.display('파이썬 리스트로 구현한 리스트 테스트')
#3
print(l.find(101))
#4
li=[1,2,10]
l.merge1(li)
l.display('파이썬 리스트로 구현한 리스트 테스트')
