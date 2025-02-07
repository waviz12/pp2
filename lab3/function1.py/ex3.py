#me need find counts of chicken and rabbit()
#i know that count of head is 35 and legs is 94
#solution this func
def solve(numheads, numlegs):
    chickens=-1*((numlegs-4*numheads)/2)
    rabbits=numheads-chickens
    return chickens,rabbits




print(solve(35,94))