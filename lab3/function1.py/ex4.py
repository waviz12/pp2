x = []
y = int(input())
for i in range(y):
    num = int(input())
    x.append(num)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_of_prime(numbers):
    result = []
    for num in numbers:
        if is_prime(num):
            result.append(num)
    return result

print("Простые числа:", filter_of_prime(x))



