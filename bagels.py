from random import randint

MAX_TRIALS = 10
trials = 0

print("Bagels, a deductive logic game. \
By Al Sweigart al@inventwithpython.com \
I am thinking of a 3-digit number. Try to guess what it is. \
Here are some clues: \
When I say: That means: \
Pico One digit is correct but in the wrong position. \
Fermi One digit is correct and in the right position. \
Bagels No digit is correct. \
I have thought up a number. \
You have 10 guesses to get it.")

number_random = randint(100, 999)
number_random_array = list(str(number_random))
#print(number_random_array)

while trials < MAX_TRIALS:
    number_str = input("Enter a three digit number: ")
    number_array = list(number_str)
    #print(number_array)

    # Compare the user input with the random number
    for i in range(3):
        if number_array[i] == number_random_array[i]:
            print("Fermi")
        elif number_array[i] in number_random_array:
            print("Pico")
        else:
            print("Bagel")

    trials += 1

    # Break loop if user has guessed the right number
    if number_array == number_random_array:
        print("Congratulations, you have got the number!")
        break
    else:
        print("Sorry, try again!")

else:
    print("You have exhausted all your chances!")