#RECEIVING AND RETURNING VALUES PROGRAM
#Demonstrates receiving and returning function vales and information.

def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """ Ask a yes or no question """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        return response

#Main
print("Here is the function message for you\n")

number = give_me_five()
print("Here is the function number given to me: ", number)

answer = ask_yes_no("\nPlease enter 'y' or a 'n': ")
print("Thank you for your answer: ", answer)