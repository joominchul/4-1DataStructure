class Node:
    def __init__ (self, elem, link=None):
        self.data = elem
        self.link = link
class LinkedQueue:
    def __init__( self ):
        self.front = None
        self.rear=None
    def isEmpty( self ): return self.rear == None
    def enqueue(self, item) :
        node=Node(item,None)
        if self.isEmpty():
            self.rear=node
            self.front=node
        else:
            self.rear.link=node
            self.rear=node
    def dequeue(self):
        if not self.isEmpty():
            data=self.front.data
            if self.front==self.rear:
                self.rear=None
            else:
                self.front=self.front.link
            return data
    def peek(self):
        if not self.isEmpty():
            return self.front.data
    def display( self, msg='LinkedQueue:'):
        print(msg, end='')
        node = self.front
        while not node == None :
            print(node.data, end=' ')
            node = node.link
        print()
print("연결된 구조의 큐 구현\n")
queue=LinkedQueue()
for i in range(10):
    queue.enqueue(i)
queue.display("큐 enqueue 9회:")
print('\tdequeue()__>',queue.dequeue())
print('\tdequeue()__>',queue.dequeue())
print('\tdequeue()__>',queue.dequeue())
queue.display('큐 dequeue 3회:')
print('\tpeek()__>',queue.peek())