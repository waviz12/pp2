import math
y=math.pi
def func(x):
    radians=x*(y/180)
    print(f"Output radian: {radians:.6f}")
x=float(input())
func(x)