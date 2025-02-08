def uniquelist(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

mylist = list(map(int, input("numbers of list: ").split()))
print(uniquelist(mylist))