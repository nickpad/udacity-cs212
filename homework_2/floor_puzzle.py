#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def not_adjacent(a, b):
    return abs(a - b) != 1

def floor_puzzle():
    for occupants in itertools.permutations((1,2,3,4,5)):
        Hopper, Kay, Liskov, Perlis, Ritchie = occupants
        if (Hopper != 5) and (Kay != 1) and (Liskov not in (1,5)) and \
        (Perlis > Kay) and not_adjacent(Ritchie, Liskov) and \
        not_adjacent(Liskov, Kay): return list(occupants)

print(floor_puzzle())