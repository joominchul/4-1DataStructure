import queue
#5.15 오른쪽 문제
v=queue.Queue()
for i in range(20):
    if i%3==0:
        v.put(i)
    elif i%4==0:
        print(v.get())
while not v.empty():
    print("/",v.get())
