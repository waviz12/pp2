import re 

with open("/Users/daniyartanerbergen/Documents/PP2/labs/lab5/row.txt", encoding="utf-8") as file:
    data = file.read()

m = re.findall("ab{2,3}", data)
print(m)