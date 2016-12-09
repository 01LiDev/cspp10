import random
def piggy_bank():
    piggy_bank = int(100)
    return piggy_bank
def player_bet():
    print ("Bank Amount: {}".format (piggy_bank()))
    user_bet=input("Enter a whole number or type hold:")
    return user_bet
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
    total_win = 0
    house_turn = dices()
    detector = validator()
    bank = piggy_bank()
    point_dice=point_roll()
    while detector == "valid":
        print ("You bet {}".format(player_bet()))
        if first_roll() == "win":
            total_win = player_bet() + player_bet()
            bank = bank +total_win
            print ("You won")
            print ("You now have {}$".format(bank))
        elif point_dice == "win":
            total_win = player_bet() + player_bet()
            bank = bank + total_win
            print ("You won")
            print ("You now have {}$".format(bank))
        elif first_roll() == "lost":
            bank = bank - player_bet()
            print ("You lost to house")
            print ("You now have {}$".format(bank))
        elif point_dice == "lost":
            bank = bank - player_bet()
            print ("You lost to house")
            print ("You now have {}$".format(bank))
        elif validator() == "holded":
            print ("player holded bank amount {}$".format(bank))
        
           
    
craps()
 
