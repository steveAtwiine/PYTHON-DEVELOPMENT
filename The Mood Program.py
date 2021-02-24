##The Mood Program
#This program checks to see how your mood is

#Import the Random Module
import random

print ("\t\t\tHello Python Programmer, Welcome to the Mood Program")
print("\n\t\t\tChoose from a given range between 0 - 3 and I\'ll tell you your moods today...")


mood = random.randint(0, 3)
mood = int(input("\n\t\t\tWhat is your mood today...."))

if mood == 0:
    print("\n\t\t\tYour mood is poor")
elif mood == 1:
    print("\n\t\t\tYour mood is low")
elif mood == 2:
    print("\n\t\t\tYour mood is medium")
elif mood == 3:
    print("\n\t\t\tYour mood is high")
else:
    print("\n\t\t\tYour moods are unclear...")