#AN EXCEPTIONS ARGUMENT

try:
    num = float(input("Enter a decimal value: "))
except ValueError as e:
    print("That was not a decimal mnumber ...")
    print(e)
else:
    print("You enterred: ", num)