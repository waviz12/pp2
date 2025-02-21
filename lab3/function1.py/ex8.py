def spy_game(nums):
    code = [0, 0, 7]  
    code_i = 0  
    
    for num in nums:
        if num == code[code_i]:
            code_i += 1
        if code_i == 3:  
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False