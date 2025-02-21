import math
def func(x,y):
    area=math.ceil(sides/4*pow(length,2)*math.tan(math.pi/sides))
    print(area)
sides=int(input())
length=int(input())
func(sides,length)