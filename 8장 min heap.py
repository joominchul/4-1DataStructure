class MinHeap :
    def __init__ (self) :
        self.heap = []
        self.heap.append(0)

    def size(self) : return len(self.heap) - 1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '힙 트리: ') :
        print(msg, self.heap[1:])

    def insert(self, n) :
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n < self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self) :
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child<self.size() and self.Left(parent)>self.Right(parent):
                    child += 1
                if last <= self.heap[child] :
                    break;
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2;

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

heap = MinHeap()
data = [3,6,7,12,13,15,20]
print("[삽입 연산]: ", data)
for elem in data :
    heap.insert(elem)
heap.display('[ 삽입 후 ]: ')
heap.delete()
heap.display('[ 삭제 후 ]: ')
heap.delete()
heap.display('[ 삭제 후 ]: ')

#======================================================================
# 8.6절
#======================================================================
def make_tree(freq):
    heap = MinHeap()
    for n in freq :
        heap.insert(n)

    for i in range(0, n) :
        e1 = heap.delete()
        e2 = heap.delete()
        heap.insert(e1 + e2)
        print(" (%d+%d)" % (e1, e2))

label = [ 'E', 'T', 'N', 'I', 'S' ]
freq  = [15, 12, 8, 6, 4 ]
make_tree(freq)
#----------------------------------------------------------------------