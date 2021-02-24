#THE HERO'S INVENTORY PROGRAMME
#This programme demonstrates the creation and the use of Turples

#Creating an empty Turple
inventory = ()

#Treat the turple as a condition
if not inventory:
    print("You are empty-handed")

print("\n")

input("Press the enter key to continue ... ")

print("\n")

#Creating a turple with some elements
inventory = (
    "Swords",
    "Knives",
    "Bombs",
    "Shield",
    "Armour",
    "Healing doze"
)

#Print the turple
print("\n")

print("The turple inventory is: ")
print(inventory)

print("\n")

#Printing each element in a turple separately
print("Your items are: ")
for item in inventory:
    print(item)

print("\n")

input("Press the Enter key to exit program ... ")