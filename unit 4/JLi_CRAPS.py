import random
def piggy_bank():
    piggy_bank = int(100)
    return piggy_bank
def player_bet():
    print ("Bank Amount: {}".format (piggy_bank()))
    user_bet = input("Do want to hold?[yes:no]:")
    bet = user_bet
    while bet != "yes" or bet != "no":
        if bet == "yes":
            return "hold"
            break
        if bet == "no":   
            bet= int(input("Enter a whole number:"))
            return player_bet()
        else:
            print ("Try Again!")
            user_bet = input("Do want to hold?[yes:no]:")
            bet = user_bet 
def validator():
    while player_bet() < 1 or player_bet() > 100:
        if player_bet() < 1:
            print("Invalid amount")
        elif player_bet() > piggy_bank():
            print("You don't have enough ")
        elif player_bet() != int():
            print("Not a whole number")
        elif player_bet() == "hold":
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
    player = player_bet()
    roll_dices=dices()
    total_win = 0
    detector = validator()
    bank = piggy_bank()
    point_dice=point_roll()
    if detector == "valid":
        print ("You bet {}".format(player))
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
        
           
    
craps()
