#THE PRIVATE CRITTER PROGRAMME
#The programme demonstrates the use of private variables and private methods

class Critter(object):
    """ A Virtual Pet"""
    def __init__(self, name, mood):
        print("A new Critter Object has been born.")
        self.name = name        #creating a public attribute
        self.__mood = mood      #creating a private attribute

    def talk(self):
        print("I am ", self.name)
        print("Right now I feel ", self.__mood, "\n")

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        self.__private_method()

    def __str__(self):
        rep = "Object Identity\n"
        rep += "name: " + self.name + "\n"
        return rep

#MAIN
crit = Critter(name="Stephen", mood="unhappy and worried")
crit.talk()
crit.public_method()
print(crit)