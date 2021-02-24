#Craps Roller Game
#A random number Dice Roller
#Demostrates the use of random numbers

import random

#Generate numbers from 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("\nYou rolled a ", die1, "and a", die2, "for a total of", total)