#!/usr/bin/python
import matplotlib.pyplot as plt
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
    rule.rule1(amount_water, amount_coffee)
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 130])
    # plt.savefig('demo.png', bbox_inches='tight')
    # # plt.show()

if __name__ == '__main__':
    main()