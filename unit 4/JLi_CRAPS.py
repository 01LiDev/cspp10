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
def validator(user_bet):
    the_bet = user_bet
    while the_bet < 1 or the_bet > 100:
        if the_bet < 1:
            print("Invalid amount")
        elif the_bet > the_bet:
            print("You don't have enough ")
        elif the_bet != int():
            print("Not a whole number")
        elif the_bet == "hold":
            return "holded"
        
    return "valid"
def dices():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum_dice = dice_1 + dice_2
    return sum_dice
def first_roll():
    if dices() == 2 or dices() == 3 or dices() == 12:
        return "lost"
    if dices() == 7 or dices() == 11:
        return "win"
        
def point_roll():
    if dices() == 7 :
        return "lost"
    elif dices() == dices():
        return "win"
def craps():
    print ("Game Start")
    roll_dices=dices()
    total_win = 0
    detector = validator(user_bet)
    bank = piggy_bank()
    point_dice=point_roll()
    if detector == "valid":
        player = player_bet()
        print ("You bet {}$".format(player))
        print ("House rolled {} ".format(roll_dices))
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
        elif validator(user_bet) == "holded":
            print ("player holded bank amount {}$".format(bank))
        
craps()
