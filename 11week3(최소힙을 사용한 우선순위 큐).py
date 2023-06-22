class MinHeap :
    def __init__ (self) :
        self.heap = []
        self.heap.append((0,0))

    def size(self) : return len(self.heap) - 1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '우선순위 큐:') :
        print(msg, self.heap[1:])

    def insert(self, n) :
        self.heap.append(n)
        num=n[1]
        i = self.size()
        while (i != 1 and num < self.Parent(i)[1]):
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
                if child<self.size() and self.Left(parent)[1]>self.Right(parent)[1]:
                    child += 1
                if last[1] <= self.heap[child][1] :
                    break;
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

class PQueueHeap :
    def __init__( self ):
        self.heap=MinHeap()

    def isEmpty( self ):
        return self.heap.isEmpty()
    def size( self ): return len(self.items)

    def display(self):
        self.heap.display()

    def enqueue( self, n):
        self.heap.insert(n)

    def dequeue( self ):
        return self.heap.delete()

q=PQueueHeap()
q.enqueue(('Kim',90))
q.enqueue(('Lee',75))
q.enqueue(('Choi',25))
q.enqueue(('Chung',55))
q.display()

print("Dequeue Min Priority = ",q.dequeue())

q.enqueue(('Sung',27))
q.enqueue(('Kho',45))
q.enqueue(('Park',15))
q.display()
while not q.isEmpty():
    print("Dequeue Min Priority = ", q.dequeue())