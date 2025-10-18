import random

def guess_the_number():
    score = 0
    print("Welcome!To Guess the number Game!")
    print("Guess the numebr between 1-10\n")
    while True:
        number_to_guess = random.randint(1,10)
        attempts = 0
        while True:
            try:
                guess =int(input("Enter your own guess:"))
                attempts = attempts + 1

                if guess < number_to_guess:
                    print("Too low.Please try again!")
                elif guess > number_to_guess:
                    print("Too high.Please try again!")
                else:
                    print("Correct!You have guessed it right!")
                    print(f"You have guessed it in {attempts} attepmts")
                    score = score + 1
                    print(f"Your score is {score}\n")
                    break
            except ValueError:
                    print("Invalid choice.Give a number between 1-10")
guess_the_number()
