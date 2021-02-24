##THE PIZZA SLICER PROGRAMME
#This programme demonstrates string slicing.

word = "PIZZA"

print(
    """
    Slicing 'Cheat Sheet'

    0   1   2   3   4   5
    +---+---+---+---+---+
    | P | I | I | Z | A |
    +---+---+---+---+---+
    -5  -4  -3  -2  -1  0

    """
)

print("Please enter the begining and the ending index for the pizza slicing: ")
print("Press the enter key at the 'start' to exit")

start = None

while start != "":
    start = (input("\nStart: "))

    if start:
        start = int(start)
        finish = int(input("Finish: "))


print("word[", start, ':', finish, "] is", end="")
print(word[start:finish])

print("Press the enter key to exit programme...")
