##THE LIST/ARRAY ITEM COUNTER
#This program counts the number of items in a List
#And displays each one of them on a separate line.

#Importing modules
import time

#Creating a lst
programing_languages = [
    "Python",
    "Java",
    "Lisp",
    "BASIC",
    "Ruby",
    "Swift",
    "Javascript",
    "C++",
    "C#",
    "C"
]

print("\n")

print(programing_languages)

print("\n")

print("Displaying the Programming Languages each on a seprate line using a \"FOR\" loop")

print("\n")

for item in programing_languages:
    print(item)

print("\n")

#Displaying the number of items in the list
list_length = len(programing_languages)
print("The total number of items in this list og Programming Languages is: ", list_length)

print("\n")

input("Press enter to exit the programme....")

time.sleep(5)