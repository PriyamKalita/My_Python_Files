n = 18
number_of_guesses=1
print("number of guesses is limited to only 9 times:")
while(number_of_guesses<=9):
    guess_number = int(input("guess the  number:\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n")
    else:
        print("you win\n")
        print(number_of_guesses,"number of gusses be took to finish")
        break
        print("9-number_of_guesses left")
        number_of_guesses = number_of_guesses + 1

        if(number_of_guesses>9):
            print("game over")

