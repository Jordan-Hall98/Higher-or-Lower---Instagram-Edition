import random
import os
from igdata import data
from logos import logo, vs


#Clear screen
os.system('cls')

#Define a function for formating data
def format_data(account):
    '''Takes the account data and returns data into a printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

#Define a function for checking if the answer is correct
def check_answer(guess, a_followers, b_followers):
    '''Takes the user guess and follower counts and returns if they got it right'''
    if a_followers > b_followers: 
        return guess == "a"
    else:
        return guess == "b"
    
    
 

#Display logo art
print (logo)
#Set score to 0 to use as a counter
score = 0
#Randomly pick account b
account_b = random.choice(data)
#Boolean to allow game to continue
game_should_continue = True

#While loop using the game_should_continue boolean:
while game_should_continue:
    
    #Print score for the user to see
    print (f"Current score: {score}")
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    #if same account is drawn for a and b then redraw for b
    if account_a == account_b:
        account_b = random.choice(data)

    #print to user to compare A and B. Tell user how many followers A has
    print(f"Compare A: {format_data(account_a)} who has",
          account_a["follower_count"], "Million followers.")
    #print vs logo
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
   
    #take users guess
    guess = input(f"Who has more followers? Type 'A' for {account_a["name"]} or 'B' for {account_b["name"]} ").lower()

    #check the amount of followers of each
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #check if guess was accurate
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    #clear screen
    os.system('cls')
    #print logo again
    print (logo)
    #if correct add 1 to score 
    if is_correct:
        score += 1
        #give feedback
        print (f"You are right!")
    #else gameover    
    else:
        print ("")
        #let the user know their final score
        print(f"Sorry thats wrong! Final score: {score}")
        #Tell them how many followers b had so they know how much they lost by
        print(f"{account_b["name"]} has {account_b["follower_count"]} Million followers")
        #end game
        game_should_continue = False

#feedback based on total score
if score >= 6:
    print(f"Well done! A score of {score} is really good!")
else: 
    print (f"Surely you can do better than {score}")