import random

#Generate the correct guess number, in range from 1 to 20
correct_guess = random.randint(1,20)

print("Welcome to the Guess Game, number edition!")
print("The correct number is between 1 to 20, can you guess it? You have 3 attempts")

#Set the number of attempts to 3
attempt = 3


while attempt > 0: 
    guess = input("Enter you guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input, only numbers are accepted guesses.")
        continue
    if guess == correct_guess: 
        print("You are correct, well done! The correct answer is",  correct_guess)
        break
    elif guess > correct_guess: 
        print("Too high! Try again")
        attempt -= 1
        print("You have", attempt, "attempt left")
    elif guess < correct_guess: 
        print("Too low! Try again")
        attempt -= 1
        print("You have", attempt, "attempt left")
else:
    print("I´m sorry, you failed. The correct number would have been:", correct_guess)

