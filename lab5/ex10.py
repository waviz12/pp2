import re

camel = "HelloWorld"
snake = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel).lower()
print(snake)