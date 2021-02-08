import random 
from data import data 
from art import logo, vs


def pick_account():
    '''picks a random account from dataset '''
    return random.choice(data)


def print_account(account):
    '''formats data to make it more readable '''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}  {description} from {country}"

def compare_accounts(guess,followers_a, followers_b):
    ''' checks the outcome beforhand and then checks it again
    against user's answer '''
    if followers_a > followers_b:
        return guess ==  "a"
    else:
        return guess ==   "b"
    
def game():
    score = 0
    account_a = pick_account()
    account_b = pick_account()

    print(logo)
    game_on = True

    while game_on:
        account_a = account_b
        account_b = pick_account()
        compare_a = print_account(account_a)
        compare_b = print_account(account_b)
        while account_a == account_b:
            account_b = pick_account()
        
        print(f"Compare A: {compare_a}")
        print(vs)
        print(f"Compare B: {compare_b}")

        followers_a = account_a["follower_count"]
        followers_b = account_b["follower_count"]
        guess = str(input("Who has more followers? Type A/B:> ")).lower()
        if_correct = compare_accounts(guess, followers_a, followers_b)
        if if_correct:
            score += 1
            print(f"Ok! Your score is: {score}")
        else:
            print(f"You lost. With a score of: {score}")
            game_on = False

game()
again = str(input("Wanna play again? Y/N:> ")).lower()
if again == "y":
    game()

