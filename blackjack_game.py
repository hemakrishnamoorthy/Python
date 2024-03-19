import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(lst):
  if len(lst) == 2 and sum(lst) == 21:
    return 0
  elif sum(lst) > 21:
    if 11 in lst:
      lst.remove(11)
      lst.append(1)
    return sum(lst)
  else:
    return sum(lst)


def initial_deck(lst):
  for _ in range(2):
    lst.append(deal_card())


def compare(user_score, computer_score):
  if user_score == computer_score:
    print("It's a draw.")
  elif computer_score == 0:
    print("You lose. Computer has blackjack.")
  elif user_score == 0:
    print("You win. You have blackjack.")
  elif user_score > 21:
    print("You lose. You went over.")
  elif computer_score > 21:
    print("You win. Computer went over.")
  elif user_score > computer_score:
    print("You win.")
  else:
    print("You lose.")


user_cards = []
computer_cards = []
is_game_over = False
print(logo)
initial_deck(user_cards)
initial_deck(computer_cards)
while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
  else:
    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice == 'y':
      user_cards.append(deal_card())
      user_score = calculate_score(user_cards)
    else:
      is_game_over = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)

print(f"  Your final hand: {user_cards}, final score: {user_score}")
print(
    f"  Computer's final hand: {computer_cards}, final score: {computer_score}"
)
compare(user_score, computer_score)
