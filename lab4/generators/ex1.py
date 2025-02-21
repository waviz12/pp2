def squares(N):
   n = 0
   while n < N:
       yield  n**2
       n += 1

N = int(input())
squares_iter = iter(squares(N))

try:
   while True:
       print(next(squares_iter))
except StopIteration:
   pass
