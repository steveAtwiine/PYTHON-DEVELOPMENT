#THE LOOPY STRING PROGRAM
#This program takes the word you have type in and prints out each letter on a separate line making a sequence.

word = input("Please enter a word of your choice: ")

print("\n")

for letter in word:
    print(letter)

length = len(word)

print("\n")

print("The total number of words in the word typed in is: ", length)
input("Press the Enter Key to exit program")