##THE RANDOM ACCESS PROGRAM
#The program Accesses each and every element in a string by assigning it an index of its position

#Importing modules
import random

word = 'Stephen'

print("The word is: " + word, "\n")

high = len(word)
low = -len(word)

for i in range(20):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

print("\n")

input("Press the enter key to exit program...")