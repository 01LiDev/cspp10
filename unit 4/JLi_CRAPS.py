import random
def player_bet():
    user_bet = int(input("How much do you want to bet?:"))
    while user_bet < 1 or user_bet > 100:
        if user_bet < 1:
            print("Invalid amount")
        elif user_bet > user_bet:
            print("You don't have enough ")
        elif user_bet == "hold":
            return "holded"
        else:
            return user_bet
def dice_sum():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum_dice = dice_1 + dice_2
    print ("House rolled {} and {} ".format(dice_1, dice_2))
    print ("Dice total is {}".format(sum_dice))
    return sum_dice
def first_roll(sum_dice):
    point_roll = 0
    if sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        print ("You lost to house")
        return "lost"
    elif sum_dice == 7 or sum_dice == 11:
        print ("You won against house")
        return "win"
    else:
        print ("You point roll is now:{}".format(sum_dice))
        point_roll = point_roll + sum_dice
        return point_roll
        
        
def point_roll(sum_dice):
    while True:
        if point_roll == 7:
            print ("You lost to house")
            return "lost"
        elif point_roll == dice_sum():
            print ("You won against house")
            return "win"
def craps():
    print ("Game Start") 
    print ("----------")
    bank = 100
    user_bet = player_bet()
    print ("Bank:{}$".format(bank))
    print ("You bet {}$".format(user_bet))
    while bank > 0:
        sum_dice = dice_sum()
        result = first_roll(sum_dice)
        if result == "win":
            bank = bank + user_bet
            print ("You now have {}$".format(bank))
        elif point_roll == result:
            bank = bank + user_bet
            print ("You now have {}$".format(bank))
        elif result == "lost":
            bank = bank - user_bet
            print ("You now have {}$".format(bank))
        elif point_roll == "lost":
            bank = bank - user_bet
            print ("You now have {}$".format(bank))
        elif user_bet == "holded":
            print ("player holded bank amount {}$".format(bank))
            user_bet
        else:
            print ("Your Broke")
            break
craps()
