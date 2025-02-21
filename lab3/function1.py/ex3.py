#me need find counts of chicken and rabbit()
#i know that count of head is 35 and legs is 94
#solution this func
def solve(numheads, numlegs):
    #c+r=35
    #4r+2c=94
    #4*(35-c)+2c=94
    #140-4c+2c=94
    #-2c=-46
    #c=23
    chickens=-1*((numlegs-4*numheads)/2)  
    rabbits=numheads-chickens
    return chickens,rabbits




print(solve(35,94))