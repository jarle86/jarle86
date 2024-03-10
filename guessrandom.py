import random

def guess_number():
    target_numbers = [random.randint(1, 100) for _ in range(10)]
    
    print("Welcome to the Number Guessing Game!")
    print("Try to guess one of the randomly generated numbers.")
    
    a = 0

    while a < 3:
        user_guess = int(input("Enter your guess: "))
 
        if user_guess in target_numbers:
            print("Congratulations! Your guess is correct.")
            break
        elif user_guess not in target_numbers and a < 2:
            print("Sorry, your guess is incorrect. Try again!")
        a += 1

    print(f"Sorry, your guess is incorrect. The correct numbers are: {target_numbers}")

# Example usage
guess_number()