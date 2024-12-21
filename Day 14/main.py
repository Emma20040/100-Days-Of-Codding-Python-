import random
from game_data import data
from art import logo, vs

print(logo)

# randomly selecting two options from the dataset
def random_account():
    return random.choice(data)





def data_format(account):
    name = account['name']
    description= account['description']
    country= account['country']

    print(f"compare B: {name}, a {description} from {country}")

# cif the user should continue playing the game
def check_answer(guess, followers1, followers2):
    if followers1 > followers2:
         return guess == "a"
    else:
        return guess == "b"



def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random_account()
  account_b = random_account()

  while game_should_continue:
    account_a = account_b
    account_b = random_account()

    while account_a == account_b:
      account_b = random_account()

    print(f"Compare A: {data_format(account_a)}.")
    print(vs)
    print(f"Against B: {data_format(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()





