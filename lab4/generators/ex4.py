def square(a, b):
    for i in range(a,b):
        yield i ** 2

a = int(input("Print a: "))
b = int(input("Print b: "))

for i in square(a,b):
    print(i , end= ", ")