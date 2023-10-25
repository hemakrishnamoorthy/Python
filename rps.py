rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_imgs = [rock, paper, scissors]
while True:
  yr_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: \n "))
  if yr_choice < 0 or yr_choice > 2:
    print("Invalid choice")
    exit()
  print(game_imgs[yr_choice])

  comp_choice = random.randint(0, 2)
  print("Computer chose:" + game_imgs[comp_choice])
  if yr_choice == comp_choice:
    print("draw")
  elif yr_choice == 0 and comp_choice == 1:
    print("You lost")
  elif yr_choice == 0 and comp_choice == 2:
    print("Wou won!")
  elif yr_choice == 1 and comp_choice == 0:
    print("You won!")
  elif yr_choice == 1 and comp_choice == 2:
    print("You lost!")
  elif yr_choice == 2 and comp_choice == 0:
    print("You lost!")
  elif yr_choice == 2 and comp_choice == 1:
    print("You won!")
  else:
    print("Invalid choice")
    exit()

  play_again = input("Do you want to play again? (y/n) \n")
  if play_again != 'y':
    break
CP3Y9A6U


