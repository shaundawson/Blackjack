import random

def deal_card():
    """ Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack
def calculate_score(cards):
    """Take a list if cards and return score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Check for an 11 (ace). If the score is already over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) 
        cards.append(1) 
    return sum(cards)
    
#Deal the user and computer 2 cards each using deal_card()
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    #new_card = deal_card()
    #user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computers cards: {computer_cards}, current score: {computer_score}")

#If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
    