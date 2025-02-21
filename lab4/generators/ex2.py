def even(N):
    n=1
    while n<=N:
        if n%2==0:
         yield n
        n+=1



N=int(input())
myiter=iter(even(N))
try:
   while True:
       print(next(myiter))
except StopIteration:
   pass

   