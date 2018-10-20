#!/usr/bin/python
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
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

def main():
    amount_water, amount_coffee = getInput()
    amount_water = float(amount_water)
    amount_coffee = float(amount_coffee)
    y1 = rule.rule1(amount_water, amount_coffee)
    y2 = rule.rule2(amount_water, amount_coffee)
    y3 = rule.rule3(amount_water, amount_coffee)
    y4 = rule.rule4(amount_water, amount_coffee)
    y5 = rule.rule5(amount_water, amount_coffee)
    y6 = rule.rule6(amount_water, amount_coffee)
    y7 = rule.rule7(amount_water, amount_coffee)
    y8 = rule.rule8(amount_water, amount_coffee)
    y9 = rule.rule9(amount_water, amount_coffee)
    y10 = rule.rule10(amount_water, amount_coffee)
    y11 = rule.rule11(amount_water, amount_coffee)
    y12 = rule.rule12(amount_water, amount_coffee)
    y13 = rule.rule13(amount_water, amount_coffee)
    y14 = rule.rule14(amount_water, amount_coffee)
    y15 = rule.rule15(amount_water, amount_coffee)
    y16 = rule.rule16(amount_water, amount_coffee)
    y17 = rule.rule17(amount_water, amount_coffee)
    y18 = rule.rule18(amount_water, amount_coffee)
    y19 = rule.rule19(amount_water, amount_coffee)
    y20 = rule.rule20(amount_water, amount_coffee)
    y21 = rule.rule21(amount_water, amount_coffee)
    y22 = rule.rule22(amount_water, amount_coffee)
    y23 = rule.rule23(amount_water, amount_coffee)
    y24 = rule.rule24(amount_water, amount_coffee)
    y25 = rule.rule25(amount_water, amount_coffee)


    
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 130])
    # plt.savefig('demo.png', bbox_inches='tight')
    # # plt.show()

if __name__ == '__main__':
    main()