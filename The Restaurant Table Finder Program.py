##The Restaurant Table Finder Program
#This program helps you find a table to sit 
#At the restaurant, if you have some dollars,
#It will automatically find you a seat, unless otherwise...

print("\t\t\tHello There, Welcome to Maama Food Restaurant")

money = int(input("\t\t\tHow many dollars do you have..."))

print("\n")

if money > 0:
    print("\t\t\tYo Lucky, there\'s a table reserved already...")
else:
    print("\t\t\tSorry, I think you will have to wait a bit longer")
    