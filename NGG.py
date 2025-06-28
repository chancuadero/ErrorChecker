# NGG - Number Guessing Game

#import random module
import random

# built-in python function - randrange (generates random number between 0-11)
n = random.randrange(1, 11)

def Game():
    
    guess = 0 # initialize guess variable and set it to 0
    attempt = 0 #initialize attempt variable and set it to 0

    while guess != n:

        guess = int(input("Enter a number from 1 - 10\n"))
        attempt += 1 #increate attempt by 1

        if guess > 10 and guess < 0:
            print("Please enter a number from 1 - 10 only")
        elif guess > n:
            print("Too high!. Please try again.")
        elif guess < n:
            print("Too low!. Please try again.")
        else:
            print("Awesome! You got it right!")
            print(f"Attempts: {attempt}")
            break

if __name__ == "__main__":
    Game()
    print("Thanks for playing!")


