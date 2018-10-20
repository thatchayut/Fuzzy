import matplotlib.pyplot as plt
import numpy as np
import coffee
import water
import bitter

# if water = vlow and coffe = vlow -> bitter is med
def rule1(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member coffee = " + str(member_coffee))

    alpha = min(member_water, member_coffee)
    print("alpha = " + str(alpha))

    # calculate output for this rule
    output = min(alpha,1)
    x = np.arange(2, 4.2, 0.2)
    y = []
    for i in range(0,len(x)):
        y.append(round(bitter.med(x[i], alpha), 2))
    print(x)
    print(y)
    plt.plot(x, y)
    plt.savefig('rule1.png', bbox_inches='tight')