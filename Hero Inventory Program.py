#Hero's Inventory Program v3


#Creating list
Inventory = ["Sword", "Powder", "Poison", "Healing Gel", "Shield"]
print("Your items are: ")
print("\n")
for item in Inventory:
    print(item)

#The lenght of the list
print("\n")
print("And you have", len(Inventory), "items in your possessions.")

#Checking if item exists
print("\n")
if "Healing Gel" in Inventory:
    print("You will live for another day")
else:
    print("You are dead meat")

#Displaying an item as per its index
index = int(input("Enter the index position of an item you want to use: "))
print("At index ", index, "you will use:", Inventory[index])

#Slicing the List
print("\n")
start = int(input("Enter the starting item that you want from your inventory: "))
finish = int(input("Enter the finishing item that you want to from your inventory: "))
print("Your Slicing results are: [", start,":",finish, "], and your items are: ")
print(Inventory[start:finish])

#Concatenating a list
print("\n")
chest = ["Gems", "Diamond", "Gold"]
print("You will find a bonquet having: ")
for item in chest:
    print(item)
print("And you will add them to your existing inventory which will now grow to: ")
Inventory+=chest
print(Inventory)


#Assigning an element into a list
print("\n")
print("You now trade your shield for an arrow")
Inventory[4] = "Arrow"
print("Your new inventory items are: ")
for item in Inventory:
    print(item)

#Assigning a new slice element
print("\n")
print("You now use your Gems and Diamond to buy an Orb of Future Telling")
Inventory[5:7] = ["Orb of Future Telling"]
print("Your newest inventory is now: ")
for item in Inventory:
    print(item)

#Deleting an item from the list
print("\n")
print("In a great battle, your Arrow is stolen by thieves")
del Inventory[4]
print("Your inventory is now")
for item in Inventory:
    print(item)

#Deleting a slice
print("\n")
print("In the middle of the struggle, you lose you sword, powder and poison")
del Inventory[:3]
print("Your inventory is now reduced to: ")
for item in Inventory:
    print(item)