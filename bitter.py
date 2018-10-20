def vbitter(input):
    member_value = 0
    if(input <= 2):
        member_value = ((-1)*input) + 2
    else:
         member_value = 0
    return member_value

def low(input):
    member_value = 0
    if(1 <= input <= 3):
        member_value = 1 - math.fabs((input - 2) / 2)
    else:
        member_value = 0
    return member_value

def med(input):
     member_value = 0
    if(2 <= input <= 4):
        member_value = 1 - math.fabs((input - 3) / 2)
    else:
        member_value = 0
    return member_value

def bitter(input):
    member_value = 0
    if(3 <= input <= 5):
        member_value = 1 - math.fabs((input - 4) / 2)
    else:
        member_value = 0
    return member_value

def vbitter(input):
    member_value = 0
    if(input >= 4):
        member_value = (input - 4)
    else:
         member_value = 0
    return member_value  
