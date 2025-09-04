# utility script 9, Number Guessing Game. 
# Python's random module provides functions for generating pseudo-random numbers 
# and performing random operations. To use it, you first need to import the module:
import random
# random.random(): Returns a random floating-point number between 0.0 (inclusive) 
# and 1.0 (exclusive).
# print(random.random())  

# random.randint(a, b): Returns a random integer N such that a <= N <= b.
num=random.randint(1,10)
guess=int(input("guess any number between 1 and 10 including 1 and 10:"))

while guess!=num:
        print(f"try again.")   
        guess=int(input("guess any number between 1 and 10 including 1 and 10:"))
 
if guess==num:
        print(f"your guess is right. you guessed {guess} and the number is also {num}")