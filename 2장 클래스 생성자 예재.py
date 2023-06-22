class Car :
    def __init__(self, color, speed=0):
        self.color=color
        self.speed=speed
    def speedUp(self):
        self.speed+=10

car1=Car('black',0)
car2=Car("red",100)
print("car1 color= %s speed= %d" % (car1.color, car1.speed))
print("car2 color= %s speed= %d" % (car2.color, car2.speed))
car1.speedUp()
print("car1 color= %s speed= %d" % (car1.color, car1.speed))