##The Losing Battle Program
#Your Hero fights trolls until he defeats all the evil 
#Aliens, but let\'s see if he remains with some life...

print("\t\t\tWelcome to the Losing Battle Game")
print("\t\t\tYour Favourite super hero fights all the aliens...")
print("\t\t\tThough let\'s see if he really remains with some life after the life...")

print("\n")

health = 10
trolls = 0
damage = 2

while health > 0:
    health -= damage
    trolls += 1

    print("\t\t\t Your super hero swings and defeats ", trolls, "trolls")
    print("\t\t\t Causing him ", damage, "of life")
    print("\t\t\tHe is left with ", health, " of his life")

    print("\n")