from stack import Stack
S1=Stack()
S2=Stack()
def enqueue(val):
    S1.push(val)
def dequeue():
    if S2.isEmpty():
        for i in range(S1.size()):
            S2.push(S1.pop())
    return S2.pop()
enqueue(1)
enqueue(2)
enqueue(3)
print("dequeue()__>", dequeue())
print("dequeue()__>", dequeue())
enqueue(4)
enqueue(5)
print("dequeue()__>", dequeue())
print("dequeue()__>", dequeue())