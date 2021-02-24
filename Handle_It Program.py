#HANDLE IT PROGRAMME
#This programme handles Exception errors and prints
#a required message instead of breaking a programme

#except/try
try:
    num = float(input("Enter a decimal number: "))
except ValueError:
    print("You have entered a wrong value")
    print("Please try enterring the correct value...")
