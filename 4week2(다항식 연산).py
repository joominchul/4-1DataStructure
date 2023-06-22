class Polynomial :
    def __init__(self):
        self.items=[]

    def degree(self):
        return len(self.items)-1

    def display(self, msg="f(x) = "):
        print(msg, end='')
        for i in range(self.degree()):
            print(self.items[i],"x^",self.degree()-i," + ",end='')
        print(self.items[self.degree()])
    def add(self, b):
        p=Polynomial()

        if self.degree() > b.degree():
            n = self.degree() - b.degree()
            for i in range(n):
                p.items.append(self.items[i])
            for i in range(b.degree()+1):
                p.items.append(self.items[i+n]+b.items[i])
        else:
            n = b.degree() - self.degree()
            for i in range(n):
                p.items.append(b.items[i])
            for i in range(self.degree()+1):
                p.items.append(b.items[i+n]+self.items[i])
        return p
    def eval(self,x):
        sum=0
        for i in range(len(self.items)):
            sum+=self.items[i]*x**(self.degree()-i)
        return sum

    def read(self):
        self.items=list(map(float,input("최고차항부터 차수를 순서대로 입력하시오: ").split()))

a=Polynomial()
b=Polynomial()
a.read()
b.read()
c=a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("A+B = ")
print("c(2) = ", c.eval(2))