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
        elif the_bet == "hold":
            return the_bet
        else:
            return the_bet
def house():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum_dice = dice_1 + dice_2
    print ("Rolled: {} and {}".format(dice_1,dice_2))
    print ("First roll:{}".format(sum_dice))
    return sum_dice
def first_roll():
    roll_1 = house()
    if roll_1 == 2 or roll_1 == 3 or roll_1 == 12:
        print ("You lost")
        return "lost"
    if roll_1 == 7 or roll_1 == 11:
        print ("You win")
        return "win"
        
def point_roll():
    point_roll = house()
    re_roll = house()
    if re_roll == 7 :
        print ("End round,You lost.")
        return "lost"
    elif re_roll == point_roll:
        print ("You win")
        return "win"
def craps():
    user_turn = player_bet()
    house_turn = house()
    detector = validator()
    bank = piggy_bank()
    if first_roll() == "win":
        bank = bank + player_bet()
    elif first_roll() == "lost":
        bank = bank - player_bet()
    elif  user_turn == "hold":
        print ("player holded bank amount {}$".format(bank))
        
           
    
craps()
 
