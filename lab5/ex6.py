import re 

with open("/Users/daniyartanerbergen/Documents/PP2/labs/lab5/row.txt", encoding="utf-8") as file:
    data = file.read()


m = re.sub(r"[., ]",':',data)
print(m)