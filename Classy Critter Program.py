#THE CLASSY CRITTER PROGRAMME
#This programme demonstrates the use of class attributes and static methods

#Creating a class
class Critter(object):
    """ A Virtual Pet """
    total = 0 #creates a class attribute of Critter Class

    @staticmethod
    def status():
        print("The number of Critter objects has now increased to ", Critter.total)

    def __init__(self, name):
        print("A new Critter Object has been born ...")
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep = "Object Item: \n"
        rep += "name: " + self.name + "\n"
        return rep

crit1 = Critter("Stephen")
crit2 = Critter("Victor")
crit3 = Critter("Simon")
crit4 = Critter("Victoria")

print(crit1)
print(crit2)
print(crit3)
print(crit4)

Critter.status()
