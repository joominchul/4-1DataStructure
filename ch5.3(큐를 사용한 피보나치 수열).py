#5.3 피보나치 수열
import queue

def pibo(q,n):
    if n==0:
        q.put(0)
        return q.get()
    elif n==1:
        q.put(1)
        return q.get()
    else:
        return pibo(q,n-1)+pibo(q,n-2)
q=queue.Queue()
print(pibo(q,6))

