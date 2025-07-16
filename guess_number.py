import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")


secret_number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! The number was", secret_number)
        break
