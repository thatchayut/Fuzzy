def vlow(input):
    member_value = 0
    if(input <= 4):
        member_value = ((-1/4)*input) + 1
    else:
         member_value = 0
    return member_value

def low(input):
    member_value = 0
    if(3 <= input <= 8):
        member_value = 1 - math.fabs((input - 5.5) / 2.5)
    else:
        member_value = 0
    return member_value

def med(input):
    member_value = 0
    if(7 <= input <= 12):
        member_value = 1 - math.fabs((input - 9.5) / 2.5)
    else:
        member_value = 0
    return member_value

def high(input):
    member_value = 0
    if(11 <= input <= 16):
        member_value = 1 - math.fabs((input - 13.5) / 2.5)
    else:
        member_value = 0
    return member_value

def vhigh(input):
    member_value = 0
    if(input >= 15):
        member_value = ((1/5)*input) - 3
    else:
         member_value = 0
    return member_value  
