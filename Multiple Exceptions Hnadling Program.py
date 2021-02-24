#MULTIPLE EXCEPTIONS HANBLING PROGRAMME
#This programme tries to handle as many exceptions at ago.

print()
for value in (None, "Hi"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number ...")
    except ValueError:
        print("I can only convert a string of digits")


