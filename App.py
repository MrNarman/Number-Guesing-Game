from random import randint
from math import ceil, log

# Taking inputs
while True:
    lower_bound = input("Enter the lower bound of your range: ")
    if lower_bound.isdigit():
        lower_bound = int(lower_bound)
        break
    else:
        print("Invalid input. Please enter a number.")

while True:
    upper_bound = input("Enter the upper bound of your range: ")
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        if upper_bound > lower_bound:
            break
        else:
            print("Invalid input. The upper bound should be greater than the lower bound.")
    else:
        print("Invalid input. Please enter a number.")

# Generating random number between lower bound and upper bound
# Formula used:   Minimum number of guessing = log2(Upper bound – lower bound + 1)
comp_random_number = randint(lower_bound, upper_bound)
number_of_guesses = ceil(log(upper_bound - lower_bound +1, 2))
print("\n\tYou have only ", number_of_guesses, " chances of guessing the number.")

count = 0
flag = False

while count < number_of_guesses:
    count += 1
    
    player_guess = int(input("Guess the number: "))

    # Condition testing
    if player_guess == comp_random_number:
        print("Congradulations. You did it in ", count, " trial(s)")
        
        #once guessed the loop will break 
        flag = True
        break
    elif player_guess > comp_random_number:
        print(f"Your guess is too high. Try again.")
    elif player_guess < comp_random_number:
        print(f"your guess is too low. Try again.")

# if all the guesses are used up
if not flag:
    print(f"\nThe number is {comp_random_number}")
    