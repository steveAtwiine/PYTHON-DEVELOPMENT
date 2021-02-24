##GUESS WORD PROGRAM v2
#The program requires the user to gues the word 
#given, the user has got tries to make up to a specified number
#and the computer will produce a yes or no message...
#The program also tells the user how many words are in the jumbled word...

#Importing Modules
import random

#Creating a list of words to pick up a jumbled word...
PROGRAMMING_LANGUAGES = [
    "Python",
    "Javascript",
    "Java",
    "LISP",
    "FOTRAN",
    "COBALT",
    "hypertext",
    "stylesheets",
    "Ruby",
    "Swift",
    "Reactjs"
]

#Pick a word from the list randomly
word = random.choice(PROGRAMMING_LANGUAGES)

#Creating a variable to use later to see if the guessed word is correct.
correct = word

#Creating a jumbled version of the word
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

print("The jumbled word is", len(jumble), "characters long.")

guess = input("Your guess: ")

print("\n")

while guess != correct and guess != "":
    print("Sorry, That\'s not it")
    guess = input("Your Guess ...")

if guess == correct:
    print("Hurayyy... You gussed it")

print("\n")

print("Thanks for playing")

print("\n")

input("Press the enter key to exit program")