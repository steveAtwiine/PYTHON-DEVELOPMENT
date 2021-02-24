#THE HERO'S INVENTORY PROGRAMME
#This programme demonstrates the creation and the use of Turples
#This is the second version of the previous programme but more advanced.

#Creating a new turple with contents in it.
#A tuple with weapons for the fight
inventory = (
    "Swords",
    "Knives",
    "Blades",
    "Shield",
    "Bows",
    "Arrows",
    "Dozing Kit"
)

print("\n")

#Displaying the items for the fight.
print("Your items for the fight are: ")

print("\n")

for item in inventory:
    print(item)

print("\n")

input("Press the enter key to continue ... ")

print("\n")

#Displaying the number of items the Hero has for the fight
print("The number of items you have for the fight are: ", len(inventory), " items")

print("\n")

#Testing to see if the life portion is available
if "Dozing Kit" in inventory:
    print("You will leave another day")
else:
    print("You will die soon")

print("\n")

#Display an item from the list
index = int(input("Please choose an item from the list ... "))
print("At index", index, "is", inventory[index])

print("\n")

#Displaying a slice
start = int(input("Enter a number to begin a slice from the weapon list: "))
finish = int(input("Enter a number to finish a slice from the weapon list: "))
print("Inventory[", start, ":", finish, "] is", end="")
print(inventory[start:finish])

input("Press the enter key to continue ... ")

#Making and Concanating a new turple
chest = (
    "Gold",
    "Gems",
    "Diamonds",
    "Excalibar"
)

print("\n")

print("You have found a new item inventory and it contains: ", len(chest), "items")
print("And these are: ")
for items in chest:
    print(items) 

#Adding new items to your original inventory
print("\n")
print("You now add new items from the discovered chest into your old inventory")
print("\n")
inventory += chest
print("\n")
print("Your inventory is now: ", inventory)


input("Press the enter key to continue")