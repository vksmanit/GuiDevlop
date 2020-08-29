number = 7

#while user_input != "n":
while True:
    user_input = input ("Would you like to play (y/n) ").lower()

    if (user_input == "n"):
        break
    user_input = int(input("Guess the number: "))
    if user_input == number : 
        print ("yes")
    elif abs(user_input - number == 1):
        print("off by one")
    else : 
        print ("sorry, whould you like to try again")
