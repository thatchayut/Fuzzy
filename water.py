import math

def vlow(input):
    member_value = 0
    if(input <= 40):
        member_value = ((-1/40)*input) + 1
    else:
         member_value = 0
    return member_value

def low(input):
    member_value = 0
    if(30 <= input <= 80):
        member_value = 1 - math.fabs((input - 55) / 25)
    else:
        member_value = 0
    return member_value

def med(input):
    member_value = 0
    if(70 <= input <= 120):
        member_value = 1 - math.fabs((input - 95) / 25)
    else:
        member_value = 0
    return member_value

def high(input):
    member_value = 0
    if(110 <= input <= 160):
        member_value = 1 - math.fabs((input - 135) / 25)
    else:
        member_value = 0
    return member_value

def vhigh(input):
    member_value = 0
    if(input >= 150):
        member_value = ((1/50)*input) - 3
    else:
         member_value = 0
    return member_value  

