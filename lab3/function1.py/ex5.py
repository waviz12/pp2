def get_permutations(string):
    if len(string) <= 1:
        return [string]
        
    perms = []
    for i, char in enumerate(string):
        remaining = string[:i] + string[i+1:]
        for p in get_permutations(remaining):
            perms.append(char + p)
    return perms

word = input("Enter a string: ")
result = get_permutations(word)
for perm in result:
    print(perm)