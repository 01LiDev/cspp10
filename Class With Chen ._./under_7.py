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
    player_bet = int(input("how much do you want to bet?-:"))
    # if player's bet is more than they have
    while player_bet > bank:
        print ("Don't have enough!!!")
        player_bet = int(input("how much do you want to bet?-:"))
    # if player's bet is valid, then return
    #   the bet
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
    else:
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
    return user_choice
# function for the main game
def gamble():
    bank = 100
    place_bet = get_bet(bank)
    choice_bet = choose_range()
    while place_bet > bank:
        first_result = roll2dice()
        choice_got = get_range(first_result)
        first_result = roll2dice()
        if choice_bet == choice_got:
            bank = bank + place_bet * 2
            print ("You Win!")
            if choice_bet == 7:
                bank = bank + place_bet * 4
        elif choice_bet != choice_got:
            print ("You Lose!")
gamble()
        
