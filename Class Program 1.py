#THE CLASS PROGRAMME 1 
#This program demonstrates the creation of the Class(BluePrint)
#And creation of Objects from this class(Instantiation)

class Critter(object):
    """ A virtual pet """
    def talk(self):
        print("Hello Python programmer, am an instantiate of the Critter class One")

#Main
crit = Critter()
crit.talk()

