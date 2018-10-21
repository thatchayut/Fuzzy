#!/usr/bin/python
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
import numpy as np
import rule

def getInput():
    check = False
    while(check == False):
        amount_water = input("Amount of water (0-200 ml) : ")
        type(amount_water)
        if((float(amount_water) >= 0) and (float(amount_water) <= 200)):
            check = True
            break
        print("Invalid input !")
    check = False
    while(check == False):
        amount_coffee = input("Amount of coffee (0-20 g) : ")
        type(amount_water)
        if((float(amount_coffee) >= 0) and (float(amount_coffee) <= 20)):
            check = True
            break
        print("Invalid input !")    
    return amount_water, amount_coffee

def  findMax(list1, list2):
    y = []
    if(len(list1) == len(list2)):
        for i in range(0, len(list1)):
            y.append(max(list1[i], list2[i]))
    return y

def main():
    amount_water, amount_coffee = getInput()
    amount_water = float(amount_water)
    amount_coffee = float(amount_coffee)
    y1 = rule.rule1(amount_water, amount_coffee)
    y2 = rule.rule2(amount_water, amount_coffee)
    y = findMax(y1, y2)
    y3 = rule.rule3(amount_water, amount_coffee)
    y = findMax(y, y3)
    y4 = rule.rule4(amount_water, amount_coffee)
    y = findMax(y, y4)
    y5 = rule.rule5(amount_water, amount_coffee)
    y = findMax(y, y5)
    y6 = rule.rule6(amount_water, amount_coffee)
    y = findMax(y, y6)
    y7 = rule.rule7(amount_water, amount_coffee)
    y = findMax(y, y7)
    y8 = rule.rule8(amount_water, amount_coffee)
    y = findMax(y, y8)
    y9 = rule.rule9(amount_water, amount_coffee)
    y = findMax(y, y9)
    y10 = rule.rule10(amount_water, amount_coffee)
    y = findMax(y, y10)
    y11 = rule.rule11(amount_water, amount_coffee)
    y = findMax(y, y11)
    y12 = rule.rule12(amount_water, amount_coffee)
    y = findMax(y, y12)
    y13 = rule.rule13(amount_water, amount_coffee)
    y = findMax(y, y13)
    y14 = rule.rule14(amount_water, amount_coffee)
    y = findMax(y, y14) 
    y15 = rule.rule15(amount_water, amount_coffee)
    y = findMax(y, y15)
    y16 = rule.rule16(amount_water, amount_coffee)
    y = findMax(y, y16)
    y17 = rule.rule17(amount_water, amount_coffee)
    y = findMax(y, y17) 
    y18 = rule.rule18(amount_water, amount_coffee)
    y = findMax(y, y18)
    y19 = rule.rule19(amount_water, amount_coffee)
    y = findMax(y, y19)    
    y20 = rule.rule20(amount_water, amount_coffee)
    y = findMax(y, y20)
    y21 = rule.rule21(amount_water, amount_coffee)
    y = findMax(y, y21)
    y22 = rule.rule22(amount_water, amount_coffee)
    y = findMax(y, y22)
    y23 = rule.rule23(amount_water, amount_coffee)
    y = findMax(y, y23)
    y24 = rule.rule24(amount_water, amount_coffee)
    y = findMax(y, y24)
    y25 = rule.rule25(amount_water, amount_coffee)
    y = findMax(y, y25)

    print("overall output (y) : ")
    print(y)
    x = np.arange(0, 5.2, 0.2)
    plt.figure(26)
    plt.plot(x, y)
    plt.savefig('overall.png', bbox_inches='tight') 
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 130])
    # plt.savefig('demo.png', bbox_inches='tight')
    # # plt.show()

if __name__ == '__main__':
    main()