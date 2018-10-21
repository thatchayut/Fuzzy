import math

def vlow(input, alpha):
    member_value = 0
    if(input <= 2):
        member_value = ((-1)*input) + 2
        if(member_value > alpha):
            member_value = alpha
    else:
         member_value = 0
    return member_value

def low(input, alpha):
    member_value = 0
    if(1 <= input <= 3):
        member_value = 1 - math.fabs((input - 2) / 1)
        if(member_value > alpha):
            member_value = alpha
    else:
        member_value = 0
    return member_value

def med(input, alpha):
    member_value = 0
    if(2 <= input <= 4):
        member_value = 1 - math.fabs((input - 3) / 1)
        if(member_value > alpha):
            member_value = alpha
    else:
        member_value = 0
    return member_value

def bitter(input, alpha):
    member_value = 0
    if(3 <= input <= 5):
        member_value = 1 - math.fabs((input - 4) / 1)
        if(member_value > alpha):
            member_value = alpha
    else:
        member_value = 0
    return member_value

def vbitter(input, alpha):
    member_value = 0
    if(input >= 4):
        member_value = (input - 4)
        if(member_value > alpha):
            member_value = alpha
    else:
         member_value = 0
    return member_value  

def convertOutput(value):
    max = 0
    if(value <= 2):
        member_value = ((-1)*value) + 2
        if(member_value >= max):
            max = member_value
            output = "very low"
    if(1 <= value <= 3):
        member_value = 1 - math.fabs((value - 2) / 1)
        if(member_value >= max):
            max = member_value
            output = "low"
    if(2 <= value <= 4):
        member_value = 1 - math.fabs((value - 3) / 1)
        if(member_value >= max):
            max = member_value
            output = "medium"
    if(3 <= value <= 5):
        member_value = 1 - math.fabs((value - 4) / 1)
        if(member_value >= max):
            max = member_value
            output = "bitter"
    if(value >= 4):
        member_value = (value - 4)
        if(member_value >= max):
            max = member_value
            output = "very bitter"
    return output



    

    
