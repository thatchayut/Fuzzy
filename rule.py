import coffee
import water

# if water = vlow and coffe = vlow -> bitter is med
def rule1(amount_water, amount_coffee):
    member_water = water.vlow(amount_water)
    member_coffee = coffee.vlow(amount_coffee)
    print("member water = " + str(member_water))
    print("member_coffee = " + str(member_coffee))