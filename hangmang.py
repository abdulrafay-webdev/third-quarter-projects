import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    secret_word = random .choice(words)
    guessed_letter = set()
    max_attempts = secret_word.__len__()*2
    attempts = max_attempts

    print("welcome to the Hangman Game!")
    print("I'm thinking of a word.")
    print("Can you guess the word?")
    print(f"The word is {len(secret_word)} letters long.")
    print(f"You have {attempts} attempts to guess the word.")

    while set(secret_word) != guessed_letter:
        display_word = "".join(letter if letter in guessed_letter else '_' for letter in secret_word)
        print(f"\nWord to guess: {display_word}")
        print(f"\nRemaining attempts: {attempts}")

        guess = input("Enter your guess letter: ").lower()
        attempts -= 1

        if guess in guessed_letter:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letter.add(guess)

        if guess in secret_word:
            print("Good guess!")
            if set(secret_word) == guessed_letter:
                print(f"Congratulations! You guessed the word {secret_word} correctly.")
                break
            else:
                print("wrong guess! Try again.")
                print(f"Remaining attempts: {attempts}")
    else:
        print(f"Game over! The word was '{secret_word}'.")        

hangman()