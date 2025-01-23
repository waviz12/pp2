#legal variable names:
myvar = "cash"
my_var = "cash"
_my_var = "cash"
myVar = "cash"
MYVAR = "cash"
myva1 = "cash"
#many values to multiplate variables
x,y,z = "odin" ,"dva", "tri"
print(x)
print(y)
print(z)
#one value to multiplate valiables
x=y=z="odin"
print(x)
print(y)
print(z)
#unpack a collection
numbers ={"one","two","three"}
x,y,z= numbers
print(x)
print(y)
print(z)
#output variable 
x= "bo bo bounce"
print(x)
#or
x="bo"
y="bo"
z="bounce"
print(x,y,z)
#global variable
x="cash"
def myfunc():
    print(x)
myfunc()  