#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 

#3 Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"] 

#4 With no if statement:
newlist = [x for x in fruits] 


#5 You can use the range() function to create an iterable:
newlist = [x for x in range(10)] 

#6 Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5] 

#7 Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits] 

#8 Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits] 

#9 Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits] 