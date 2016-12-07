import random
def piggy_bank():
    piggy_bank = int(100)
    return piggy_bank
def player_bet():
    print ("Bank Amount: {}".format (piggy_bank()))
    user_bet=int(input("Enter a whole number or type hold:"))
    return user_bet
def validator():
    the_bet = player_bet()
    while the_bet < 1 and the_bet > 100:
        if the_bet < 1:
            print("Invalid amount")
        elif the_bet > piggy_bank():
            print("You don't have enough ")
        elif the_bet != int():
            print("Not a whole number")
        else:
            return the_bet
def house():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum_dice = dice_1 + dice_2
    print ("Rolled: {} and {}".format(dice_1,dice_2))
    return sum_dice
def first_roll():
    roll_1 = house()
    while roll_1 == 2 or roll_1 == 3 or roll_1 == 12:
        print ("You lost")
        return "lost" and "house_win"
    if roll_1 == 7 or roll_1 == 11:
        print ("You win")
        return "win"
        
def point_roll():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    re_roll = dice_1 +dice_2
    if re_roll == 7 :
        print "End round,You lost."
        return "lost"
    elif re_roll == house():
        print "You win"
        return "win"
def score():
    print ("-------------")
    print ("House won {} rounds".format)
    print ("")

# def craps():
#purpose:
#arguments:
#returns:
    
    
    
# craps()
 
