import re

with open("lab5/row.txt") as file:
    data = file.read()
m = re.findall("a.*b", data)
print(m)