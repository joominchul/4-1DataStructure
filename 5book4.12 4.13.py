from stackClass import Stack
#4.12
s=Stack()
n=0
while n>0:
    s.push(n%2)
    n=n//2
while not s.isEmpty():
    print(s.pop())
#4.13
values=Stack()
for i in range(20):
    if i%3==0:
        values.push(i)
        print("push",i)
    elif i%4==0:
        print("pop",values.pop())
print(values)