import re

with open("/Users/daniyartanerbergen/Documents/PP2/labs/lab5/row2.txt", encoding="utf-8") as file:
    data = file.read()

print(re.sub(r"([A-Z])", r" \1", data))