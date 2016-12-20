import random
def piggy_bank():
    piggy_bank = int(100)
    return piggy_bank
def player_bet():
    print ("Bank Amount: {}$".format (piggy_bank()))
    user_bet = int(input("How much do you want to bet?:"))
    return user_bet
def validator(user_bet):
    while user_bet < int(1) or user_bet > int(100):
        if user_bet < int(1):
            print("Invalid amount")
        elif user_bet > user_bet:
            print("You don't have enough ")
        elif user_bet != int():
            print("Not a whole number")
        elif user_bet == "hold":
            return "holded"
        else:
            return "valid"
def dice_1():
    dice_1 = int(random.randint(1,6))
    return dice_1
def dice_2():
    dice_2 = int(random.randint(1,6))
    return dice_2
def dice_sum(dice_1, dice_2):
    sum_dice = dice_1 + dice_2
    return sum_dice
def first_roll(sum_dice):
    if sum_dice == int(2) or sum_dice == int(3) or sum_dice == int(12):
        return "lost"
    if sum_dice == int(7) or sum_dice == int(11):
        return "win"
        
def point_roll(sum_dice):
    if sum_dice == int(7) :
        return "lost"
    elif sum_dice == sum_dice:
        return "win"
def craps():
    print ("Game Start") 
    dice_1 = dice_1()
    dice_2 = dice_2()
    total_dice = dice_sum(dice_1, dice_2)
    user_bet = player_bet()
    total_win = int(0)
    detector = validator(user_bet)
    bank = piggy_bank()
    point_dice=point_roll(sum_dice)
    while detector == "valid":
        print ("You bet {}$".format(user_bet))
        print ("House rolled {} and {} ".format(dice_1, dice_2)
        print ("Dice total is {}".format(total_dice))
        if first_roll(sum_dice) == "win":
            total_win = user_bet + user_bet
            bank = bank +total_win
            print ("You won")
            print ("You now have {}$".format(bank))
        elif point_dice == "win":
            total_win = user_bet + user_bet
            bank = bank + total_win
            print ("You won")
            print ("You now have {}$".format(bank))
        elif first_roll(sum_dice) == "lost":
            bank = bank - user_bet
            print ("You lost to house")
            print ("You now have {}$".format(bank))
        elif point_dice == "lost":
            bank = bank -user_bet
            print ("You lost to house")
            print ("You now have {}$".format(bank))
        elif validator(user_bet) == "holded":
            print ("player holded bank amount {}$".format(bank))
        else:
            break
craps()
