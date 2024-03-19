import random

logo = """
  ________                                __  .__              _______               ___.                ._.
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________| |
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ |
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\|
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   __
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       \/

"""
print(logo)
print("Welcome to the number guessing game!\n")
print("I am thinking of a number between 1 and 100.\n")
number = random.randint(1, 100)
level = input("Choose a difficulty level: 1 for easy or 2 for  hard: ")
if level == "1":
  attempts = 10
  print("You have 10 attempts to guess the number. ")
elif level == "2":
  attempts = 5
  print("You have 5 attempts to guess the number. ")
else:
  print("You have entered an invalid level. ")


def check_guess(guess, answer):
  if guess > answer:
    print("Too high. Guess again. ")
  else:
    print("Too low. Guess again.")

for i in range(attempts):
  guess = int(input("Make a guess: "))
  if guess == number:
    print("You guessed it right. You win! ")
    break
  check_guess(guess, number)
  attempts -= 1
  print(f"You have {attempts} attempts left. ")

if attempts == 0 and not is_guess_right:
  print("You have run out of attempts. You lose. ")
