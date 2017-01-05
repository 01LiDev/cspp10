import random

# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice_1 = random.randint(1,6)
    # generate another random number from 1 to 6
    dice_2 = random.randint(1,6)
    # get the sum of the two rolls
    first_result = dice_1 + dice_2
    # print the sum
    print ("dice rolled are {} and {},total is {}".format(dice_1,dice_2,first_result))
    # return the sum
    return first_result
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
    player_bet = int(input("how much do you want to bet?" " "))
    # if player's bet is more than they have
    if player_bet < bank:
        print "Don't have enough!!!" + player_bet
    # if player's bet is valid, then return
    #   the bet
    elif player_bet > bank:
         return player_bet

# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(first_result):
    # if the sum is over 7, return "over7"
    if first_result < 7:
        return "over7"
    # if the sum is under 7, return "under7"
    elif first_result > 7:
        return "under7"
    # if the sum is 7, return "equal7"
    elif first_result == 7:
        return "equal7"
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
    user_choice = input("What do you think it is?[over7:under7:equal7]")
    while user_choice != "over7" or user_choice != "under7" or user_choice != "equal7":
        print ("Enter a correct choice.....")
        user_choice
    # return their choice
    else:
        return user_choice
# function for the main game
def gamble():
    choice_result = get_range(first_result)
    
