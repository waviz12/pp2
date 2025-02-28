import re

with open("lab5/row2.txt") as file:
    data = file.read()

print(re.sub(r"([A-Z])", r" \1", data))