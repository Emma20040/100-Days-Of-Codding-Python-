import random
from art import logo
def deal_card():
    cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(cards)
    return card

def calculate_score(cards):
    '''take a list of acrds and return score calculated from the cards'''
    if  sum(cards) ==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "it's a draw🤯"
    elif computer_score ==0:
        return "you lose user has black jack😭"
    elif user_score == 0:
        return "win with ablackjack😎"
    elif user_score >21:
        return "you went over the normal score you lose😭 "
    elif computer_score >21:
        return "you went over the score so you win 😎"
    elif user_score > computer_score:
        return "you win 😎"
    else:
        return "you lose 😭"

def play_game():
    print(logo)
    user_cards= []
    computer_cards =[]
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your card: {user_cards}, Current score: {user_score}")
        print(f" computer first card: {computer_cards[0]} ")

        if user_score ==0 or computer_score ==0 or user_score> 21:
            is_game_over= True
        else:
            user_should_deal= input("type 'y' to get another card or type 'n' to pass ").lower()
            if user_should_deal =="y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_score)

    print(f" Your final hand{user_cards}, final score: {user_score} ")
    print(f" Computer's final hand {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play the game of black jack 'y' or 'n' ") == "y":
    play_game()