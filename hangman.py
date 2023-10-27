import hangman_words
import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

chosen_word = random.choice(hangman_words.word_list)
display_list = []
guessed_word = ""
lives = 6
guess_list = []
print(logo)
for _ in range(len(chosen_word)):
    display_list += '_'
print(''.join(display_list))

guess = input("Please guess a letter: ".lower())
while chosen_word != ''.join(display_list):
    if guess not in guess_list:
        guess_list.append(guess)
    else:
        print("You already guessed that letter!")
        guess = input("Please guess a letter: ".lower())

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display_list[i] = guess

    if guess not in chosen_word:
        print(stages[lives])
        lives -= 1

    if lives != -1:
        print(''.join(display_list))
        if chosen_word != ''.join(display_list):
            guess = input("Please guess a letter: ").lower()
        else:
            print("Game Over! You guessed the word")
            exit()
    else:
        print(f"The word to guess was: {chosen_word}")
        print("Game Over! You ran out of lives")
        exit()
