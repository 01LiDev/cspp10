import random
def get_p1_move():
    player_action = input("R;P;S: ")
    return player_action
def get_comp_move():
    comp_action= random.choice( ['R', 'P', 'S'] )
    return comp_action
def get_rounds():
    user_rounds=input.list(1,10("Rounds:"))
    return user_rounds
#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    if p1move > cmove:
        return p1move
    elif cmove > p1move:
        return cmove
    else:
        return tie

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    R = "Rock"
    P = "Paper"
    S = "Scissors"
    
    

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    score = [0,0]
    return 1
    #code here

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    tie = int(0)
    if player_action == "R" and comp_action == "s":
        return player_action 1
    elif "r" == "r":
        
    
    print(get_comp_move())

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
def test():
    return 1
    #code here

rps()
