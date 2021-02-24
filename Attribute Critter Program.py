#ATTRIBUTE CRITTER PROGRAMME
#Demonstrates creating and accessing object attributes

class Critter(object):
    """ A virtual pet"""
    def __init__(self, name): #Initialising a constructor
        print("A new critter has been created")
        self.name = name #Creating an attribute "name" for the class Critter

    def __str__(self):
        rep = "Critter Object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Hi, I am ", self.name, "\n")

#MAIN
crit1 = Critter("Poacher")
crit1.talk()

crit2 = Critter("Stephen")
crit2.talk()

print("Printing Crit1: ")
print(crit1)

print("Printing Crit2: ")
print(crit2)

print("Directly Accessing crit1.name: ")
print(crit1.name)