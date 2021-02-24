##THE MESSAGE ANALYZER PROGRAM
#This program analyzes and checks to see if a particular word is in the message
#typed in.

#Importing time
import time

print("\t\t\t\\\\\\\tTHE MESSAGE ANALYZER PROGRAM\t\\\\\\")
print("\t\t\t\t____________________________")

print("\n")

name = input("Please provide your names: ")

message = input("Please Enter your message about God: ")

time.sleep(5)

print("\n")

if "giver" in message:
    print(name + ", You are a true believer")
else:
    print(name + ", Just leave me alone evil you ...")

print("\n")

input("Press Enter key to exit program...")