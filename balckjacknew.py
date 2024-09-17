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
print(logo)

def card_select():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        print("Draw")
    elif user_score == 0:
        print("User wins with a Blackjack!")
    elif comp_score == 0:
        print("Computer wins with a Blackjack!")
    elif user_score > 21:
        print("User loses, Computer wins!")
    elif comp_score > 21:
        print("Computer loses, User wins!")
    elif user_score > comp_score:
        print("User wins!")
    else:
        print("Computer wins!")

def play_game():
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(card_select())
        comp_cards.append(card_select())

    game_on = True
    while game_on:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        
        print(f"Your cards are: {user_cards}, current score is: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_on = False
            print("Game over!")
        else:
            add_card = input("Do you want to add another card: Yes or No?\n").lower()
            if add_card == "yes":
                user_cards.append(card_select())
            else:
                game_on = False

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(card_select())
        comp_score = calculate_score(comp_cards)
    
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    compare(user_score, comp_score)

def main():
    play_game()
    while input("Do you want to play again? Yes or No:\n").lower() == "yes":
        print("\n" * 100)
        play_game()

main()
