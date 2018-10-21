import matplotlib.pyplot as plt
import numpy as np
import coffee
import water
import bitter

# if water = vlow and coffee = vlow -> bitter is med
def rule1(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.med(x[i], alpha), 2))
    print("rule 1 x: " + str(x))
    print("rule 1 y: " + str(y))
    print()
    plt.figure(1)   
    plt.plot(x, y)
    plt.savefig('rule1.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = low and coffee = vlow -> bitter is low
def rule2(amount_water, amount_coffee):
    member_water = water.low(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.low(x[i], alpha), 2))
    print("rule 2 x: " + str(x))
    print("rule 2 y: " + str(y))
    print()
    plt.figure(2)   
    plt.plot(x, y)
    plt.savefig('rule2.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = med and coffee = vlow -> bitter is vlow
def rule3(amount_water, amount_coffee):
    member_water = water.med(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vlow(x[i], alpha), 2))
    print("rule 3 x: " + str(x))
    print("rule 3 y: " + str(y))
    print()
    plt.figure(3)   
    plt.plot(x, y)
    plt.savefig('rule3.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = high and coffee = vlow -> bitter is vlow
def rule4(amount_water, amount_coffee):
    member_water = water.high(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vlow(x[i], alpha), 2))
    print("rule 4 x: " + str(x))
    print("rule 4 y: " + str(y))
    print()
    plt.figure(4)   
    plt.plot(x, y)
    plt.savefig('rule4.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vhigh and coffee = vlow -> bitter is vlow
def rule5(amount_water, amount_coffee):
    member_water = water.vhigh(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vlow(x[i], alpha), 2))
    print("rule 5 x: " + str(x))
    print("rule 5 y: " + str(y))
    print()
    plt.figure(5)   
    plt.plot(x, y)
    plt.savefig('rule5.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vlow and coffee = low -> bitter is bitter
def rule6(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.low(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 6 x: " + str(x))
    print("rule 6 y: " + str(y))
    print()
    plt.figure(6)   
    plt.plot(x, y)
    plt.savefig('rule6.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = low and coffee = low -> bitter is med
def rule7(amount_water, amount_coffee):
    member_water = water.low(amount_water)
    member_coffee = coffee.low(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 7 x: " + str(x))
    print("rule 7 y: " + str(y))
    print()
    plt.figure(7)   
    plt.plot(x, y)
    plt.savefig('rule7.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = med and coffee = low -> bitter is low
def rule8(amount_water, amount_coffee):
    member_water = water.med(amount_water)
    member_coffee = coffee.low(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.low(x[i], alpha), 2))
    print("rule 8 x: " + str(x))
    print("rule 8 y: " + str(y))
    print()
    plt.figure(8)   
    plt.plot(x, y)
    plt.savefig('rule8.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = high and coffee = low -> bitter is low
def rule9(amount_water, amount_coffee):
    member_water = water.high(amount_water)
    member_coffee = coffee.low(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.low(x[i], alpha), 2))
    print("rule 9 x: " + str(x))
    print("rule 9 y: " + str(y))
    print()
    plt.figure(9)   
    plt.plot(x, y)
    plt.savefig('rule9.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vhigh and coffee = low -> bitter is vlow
def rule10(amount_water, amount_coffee):
    member_water = water.vhigh(amount_water)
    member_coffee = coffee.low(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vlow(x[i], alpha), 2))
    print("rule 10 x: " + str(x))
    print("rule 10 y: " + str(y))
    print()
    plt.figure(10)   
    plt.plot(x, y)
    plt.savefig('rule10.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vlow and coffee = med -> bitter is vbitter
def rule11(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.med(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vbitter(x[i], alpha), 2))
    print("rule 11 x: " + str(x))
    print("rule 11 y: " + str(y))
    print()
    plt.figure(11)   
    plt.plot(x, y)
    plt.savefig('rule11.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = low and coffee = med -> bitter is bitter
def rule12(amount_water, amount_coffee):
    member_water = water.low(amount_water)
    member_coffee = coffee.med(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 12 x: " + str(x))
    print("rule 12 y: " + str(y))
    print()
    plt.figure(12)   
    plt.plot(x, y)
    plt.savefig('rule12.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = med and coffee = med -> bitter is med
def rule13(amount_water, amount_coffee):
    member_water = water.med(amount_water)
    member_coffee = coffee.med(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.med(x[i], alpha), 2))
    print("rule 13 x: " + str(x))
    print("rule 13 y: " + str(y))
    print()
    plt.figure(13)   
    plt.plot(x, y)
    plt.savefig('rule13.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = high and coffee = med -> bitter is low
def rule14(amount_water, amount_coffee):
    member_water = water.high(amount_water)
    member_coffee = coffee.med(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.low(x[i], alpha), 2))
    print("rule 14 x: " + str(x))
    print("rule 14 y: " + str(y))
    print()
    plt.figure(14)   
    plt.plot(x, y)
    plt.savefig('rule14.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vhigh and coffee = med -> bitter is vlow
def rule15(amount_water, amount_coffee):
    member_water = water.vhigh(amount_water)
    member_coffee = coffee.med(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vlow(x[i], alpha), 2))
    print("rule 15 x: " + str(x))
    print("rule 15 y: " + str(y))
    print()
    plt.figure(15)   
    plt.plot(x, y)
    plt.savefig('rule15.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vlow and coffee = high -> bitter is vbitter
def rule16(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.high(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vbitter(x[i], alpha), 2))
    print("rule 16 x: " + str(x))
    print("rule 16 y: " + str(y))
    print()
    plt.figure(16)   
    plt.plot(x, y)
    plt.savefig('rule16.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = low and coffee = high -> bitter is bitter
def rule17(amount_water, amount_coffee):
    member_water = water.low(amount_water)
    member_coffee = coffee.high(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 17 x: " + str(x))
    print("rule 17 y: " + str(y))
    print()
    plt.figure(17)   
    plt.plot(x, y)
    plt.savefig('rule17.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = med and coffee = high -> bitter is bitter
def rule18(amount_water, amount_coffee):
    member_water = water.med(amount_water)
    member_coffee = coffee.high(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 18 x: " + str(x))
    print("rule 18 y: " + str(y))
    print()
    plt.figure(18)   
    plt.plot(x, y)
    plt.savefig('rule18.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = high and coffee = high -> bitter is med
def rule19(amount_water, amount_coffee):
    member_water = water.high(amount_water)
    member_coffee = coffee.high(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.med(x[i], alpha), 2))
    print("rule 19 x: " + str(x))
    print("rule 19 y: " + str(y))
    print()
    plt.figure(19)   
    plt.plot(x, y)
    plt.savefig('rule19.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vhigh and coffee = high -> bitter is bitter
def rule20(amount_water, amount_coffee):
    member_water = water.vhigh(amount_water)
    member_coffee = coffee.high(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 20 x: " + str(x))
    print("rule 20 y: " + str(y))
    print()
    plt.figure(20)   
    plt.plot(x, y)
    plt.savefig('rule20.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vlow and coffee = vhigh -> bitter is vbitter
def rule21(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.vhigh(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vbitter(x[i], alpha), 2))
    print("rule 21 x: " + str(x))
    print("rule 21 y: " + str(y))
    print()
    plt.figure(21)   
    plt.plot(x, y)
    plt.savefig('rule21.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = low and coffee = vhigh -> bitter is vbitter
def rule22(amount_water, amount_coffee):
    member_water = water.low(amount_water)
    member_coffee = coffee.vhigh(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vbitter(x[i], alpha), 2))
    print("rule 22 x: " + str(x))
    print("rule 22 y: " + str(y))
    print()
    plt.figure(22)   
    plt.plot(x, y)
    plt.savefig('rule22.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = med and coffee = vhigh -> bitter is vbitter
def rule23(amount_water, amount_coffee):
    member_water = water.med(amount_water)
    member_coffee = coffee.vhigh(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.vbitter(x[i], alpha), 2))
    print("rule 23 x: " + str(x))
    print("rule 23 y: " + str(y))
    print()
    plt.figure(23)   
    plt.plot(x, y)
    plt.savefig('rule23.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = high and coffee = vhigh -> bitter is bitter
def rule24(amount_water, amount_coffee):
    member_water = water.high(amount_water)
    member_coffee = coffee.vhigh(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.bitter(x[i], alpha), 2))
    print("rule 24 x: " + str(x))
    print("rule 24 y: " + str(y))
    print()
    plt.figure(24)   
    plt.plot(x, y)
    plt.savefig('rule24.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y

# if water = vhigh and coffee = vhigh -> bitter is med
def rule25(amount_water, amount_coffee):
    member_water = water.vhigh(amount_water)
    member_coffee = coffee.vhigh(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(0, 5.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.med(x[i], alpha), 2))
    print("rule 25 x: " + str(x))
    print("rule 25 y: " + str(y))
    print()
    plt.figure(25)   
    plt.plot(x, y)
    plt.savefig('rule25.png', bbox_inches='tight')
    plt.figure(0)
    plt.plot(x,y)
    plt.savefig('total.png', bbox_inches='tight')
    return y