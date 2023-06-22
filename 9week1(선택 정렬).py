class ArrayList:
    def __init__( self ):
        self.items = []

    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ):
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
        self.items.sort()
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)

s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10);		s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);		s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")