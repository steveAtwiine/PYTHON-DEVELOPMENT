#THE HIGH SCORES PYTHON PROGRAM

scores = []
choice = None

#Displaying the Menu
while choice != "0":
    print(
        """
        HIGH SCORES

        0 - Exit
        1 - Show scores
        2 - Add a score
        3 - Delete a score
        4 - Sort Scores

        """
    )

    choice = input("Choice: ")
    print()

    #Exititng the Program
    if choice == 0:
        print("Good Bye")
    #Displaying the scores
    elif choice == 1:
        print("High Scores")
        for score in scores:
            print(score)
    #Adding a score
    elif choice == 2:
        score = int(input("What score did you get ?: "))
        scores.append(score)
    #Deleting a score
    elif choice == 3:
        score = int(input("Removing which score ?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn\'t in the scores list") 
    #Sorting the scores
    elif choice== 4:
        scores.sort(reverse = True)
    #Dealing with an Invalid choice
    else:
        print("Sorry, ",choice, "isn\'t in the valid choices list")

    print("\n")
    print("Press the enter key to exit program...")