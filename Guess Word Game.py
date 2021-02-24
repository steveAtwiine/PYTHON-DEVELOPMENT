##THE GUESS WORD GAME
#The programm generates a random word and gives you time to 
#Write the exact word..

#Importing modules..
import random
import time

#Create a sequence of words to choose from
WORDS = (
    "pythonista",
    "programming",
    "language",
    "hypertext",
    "markup",
    "stephen",
    "greatest",
    "programmer",
    "developer"
)

#Pick a word from the turple/list randomly
word = random.choice(WORDS)

#PPPPPPPPPPPPPPPP
correct = word

#Create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):] 

#Start the game
print(
    """
        Welcome to the Word Jumble!
    Unscramble the letters to make a word
(Press the enter key at the prompt to quit)

"""
)

print("\n")

print("The jumble is: ", jumble)

print("\n")

guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, That\'s not it")
    guess = input("Your Guess ...")

if guess == correct:
    print("Hurayyy... You gussed it")

print("\n")

print("Thanks for playing")

print("\n")

input("Press the enter key to exit program")