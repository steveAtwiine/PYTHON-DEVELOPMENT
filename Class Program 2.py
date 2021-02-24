#THE CLASS PROGRAMME 2 
#This program demonstrates the creation of the Class(BluePrint)
#And creation of Multiple Objects and a constructor method from this class(Instantiation)

class Critter(object):
    def __init__(self): #A constructor method used
        print("A new critter has been born")
    def talk(self):
        print("Hello Python Programmer, a new instantiate is created from the Critter class")

crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()