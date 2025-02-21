def divisible(N):
    n=1
    while n<=N:
        if n%3==0 and n%4==0:
            yield n 
        n+=1
N=int(input())
myiter=iter(divisible(N))
try:
    while True:
        print(next(myiter))
except StopIteration:
    pass