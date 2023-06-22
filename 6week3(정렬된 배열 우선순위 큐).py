class PQueueSorted:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]
    def enqueue(self,item):
        if self.isEmpty():
            self.items.append(item)
        else:
            num=0
            for i in range(self.size()):
                if self.items[i]<item:
                    num=i
            self.items.insert(num+1,item)
    def dequeue(self):
        return self.items.pop(-1)
    def peek(self):
        return self.items[self.size()-1]
q=PQueueSorted()
q.enqueue(10)
q.enqueue(34)
q.enqueue(18)
print("Peek Max Priority = ",q.peek())
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("PQueue:", q.items)
while not q.isEmpty():
    print("Dequeue Max Priority = ",q.dequeue())