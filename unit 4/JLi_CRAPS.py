import random
#funtion
#
#
#
def piggy_bank():
    piggy_bank = int(100)
    return piggy_bank
def player_bet():
    print ("Bank Amount: {}$".format (piggy_bank()))
    user_bet = int(input("How much do you want to bet?:"))
    return user_bet
def validator():
    while player_bet() < 1 or player_bet() > 100:
        if player_bet() < 1:
            print("Invalid amount")
        elif player_bet() > player_bet():
            print("You don't have enough ")
        elif player_bet() != int():
            print("Not a whole number")
        elif player_bet() == "hold":
            return "holded"
    return "valid"
def dice_1():
    dice_1 = random.randint(1,6)
    return dice_1
def dice_2():
    dice_2 = random.randint(1,6)
    return dice_2
def dice_sum():
    sum_dice = dice_1() + dice_2()
    return sum_dice
def first_roll():
    if dice_sum() == 2 or dice_sum() == 3 or dice_sum() == 12:
        return "lost"
    if dice_sum() == 7 or dice_sum() == 11:
        return "win"
        
def point_roll():
    if dice_sum() == 7 :
        return "lost"
    elif dice_sum() == dice_sum():
        return "win"
def craps():
    print ("Game Start") 
    dice1 = dice_1()
    dice2 = dice_2()
    roll_dices= dice_sum()
    total_win = 0
    detector = validator()
    bank = piggy_bank()
    point_dice=point_roll()
    player = player_bet()
    while detector == "valid":
        player = player_bet()
        print ("You bet {}$".format(player))
        print ("House rolled {} and {} ".format(dice1, dice2))
        print ("Dice total is {}".format(roll_dices))
        if first_roll() == "win":
            total_win = player + player
            bank = bank +total_win
            print ("You won")
            print ("You now have {}$".format(bank))
        elif point_dice == "win":
            total_win = player + player
            bank = bank + total_win
            print ("You won")
            print ("You now have {}$".format(bank))
        elif first_roll() == "lost":
            bank = bank - player
            print ("You lost to house")
            print ("You now have {}$".format(bank))
        elif point_dice == "lost":
            bank = bank - player
            print ("You lost to house")
            print ("You now have {}$".format(bank))
        elif validator() == "holded":
            print ("player holded bank amount {}$".format(bank))
        else:
            break
craps()
