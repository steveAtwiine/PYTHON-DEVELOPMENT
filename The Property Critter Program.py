#THE PROPERTY CRITTER PROGRAM
#Demonstrates properties

class Critter(object):
    """ A virtual Pet"""
    def __init__(self, name):
        print("A new Critter Object has been created")
        self.name = name
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A Critter name can\'t be the empty string ...")
        else:
            self.__name = new_name
            print("Name changed successfully ...")

    def talk(self):
        print("Hi, I\'m", self.name)

#MAIN
crit = Critter("Stephen")
crit.talk()

print("My name is: ", end="")
print(crit.name)