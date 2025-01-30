#<-------Boolean Values------->
print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 


#<-------Evaluate Values and Variables------->
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#<-------Most Values are True------->
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#<-------Some Values are False-------->
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
