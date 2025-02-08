class Shape: #class shape:
    def area(x):#def area(self)
        return 0  #return 0
class Square(Shape):    #class Square(self,length):
    def __init__(x,length): #def __init__(self,length):
        super().__init__()  #super().__init__()
        x.length = length    #x.length=length
    def area(x):             #x.area(self):
        return x.length **2    #

n = int(input())
square = Square(n)
print("area of ​​the square: ", square.area())
shape = Shape()
print("another: ", shape.area())
