## Fuzzy Logic (Approximate Reasoning)

  This program simulates the approximate reasoning by giving an example of the system to approximate the strength of a cup of coffee
by considering the amount of water in milliliter and the amount of coffee in gram.
  
  This program uses *Mamdani model* as a control system. The method of this program is as follows.
1. The program will ask you for the amount of water and the amount of coffee. For this program, the amount of water is in range [0,200]        and the amount of coffee is in range [0,20]. The liguistic terms of these 2 inputs are very low, low, medium, high, and very high. For      more detail, see **water.py** and **coffee.py**.
2. Rules are applied by using these input values. There are 25 rules for this system. You can find these rules in **rule.py**. The result      of each rule will be represented by graph that will be exported as an image file. 
3. After finish calculating all rules, all of the results will be *UNION* together to give the overall result. 
4. Since the limitation of Mamdani system is that its output is uninterpretable, the defuzzification procedure is conducted to covert the
   defuzzied value to the linguistic term. In this case, I decide to use the *Center of Area (Centroid)* since it provides more unique        result than other defuzzication method. 
5. The output will be shown on the terms of bitterness level that are very low, low, medium, high, and very high. For more details, see        **rule.py**. Moreover, the graph of overall output will be exported as an image file named as overall.png.

## How to execute this program?
```
  python coffee_brew.py
```

