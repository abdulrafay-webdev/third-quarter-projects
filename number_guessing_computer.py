import random

def number_guessing_computer():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess the number?")

    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:   
            guess_number = int(input("Enter your guess number: "))
            attempts +=1
            print(f"your remaining Attempt is {max_attempts - attempts}")

            if guess_number < secret_number:
                print("Too low! Try again.")

            elif guess_number > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")   

    if attempts == max_attempts:
        print(f"Sorry! You have reached the maximum attempts. The secret number was {secret_number}.")         

number_guessing_computer()        