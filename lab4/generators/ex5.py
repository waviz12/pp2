def rever_generator(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("print n: "))
for i in rever_generator(n):
    print(i,end=", ")