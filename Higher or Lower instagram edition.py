import random
import os
from igdata import data
from logos import logo, vs



os.system('cls')


def format_data(account):
    '''Takes the account data and returns data into a printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    '''Takes the user guess and follower counts and returns if they got it right'''
    if a_followers > b_followers: 
        return guess == "a"
    else:
        return guess == "b"
    
    
 

#Display logo art
print (logo)
score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    
    print (f"Current score: {score}")
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)} who has",
          account_a["follower_count"], "Million followers.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input(f"Who has more followers? Type 'A' for {account_a["name"]} or 'B' for {account_b["name"]} ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls')
    print (logo)
    if is_correct:
        score += 1
        print (f"You are right!")
        
    else:
        print ("")
        print(f"Sorry thats wrong! Final score: {score}")
        print(f"{account_b["name"]} has {account_b["follower_count"]} Million followers")
        game_should_continue = False

if score >= 6:
    print(f"Well done! A score of {score} is really good!")
else: 
    print (f"Surely you can do better than {score}")