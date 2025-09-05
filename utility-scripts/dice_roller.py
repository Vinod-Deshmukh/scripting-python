# utility script 10, randomly stimulate dice (1-6)
import random 
while True:
    diceRoll=random.randint(1,6)
    print(diceRoll)

    again=input("Roll again (y/n)?: ")
    if again.upper()!="Y":
        break