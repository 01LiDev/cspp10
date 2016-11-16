import random
def get_p1_move():
    p1move = input("Rock;Paper;Scissors: ")
    return p1move
def get_comp_move():
    cmove= random.choice( ['Rock', 'Paper', 'Scissors'] )
    return cmove
def get_rounds():
    rounds = int(input("Rounds: "))
    return rounds
def get_round_winner(p1move, cmove):
    if p1move == "Rock" and cmove == "Scissors":
        return p1move
    elif p1move == "Scissors" and cmove == "Paper":
        return p1move
    elif p1move == "Paper" and cmove == "Rock":
        return p1move
    elif cmove == "Rock" and p1move =="Scissors":
        return cmove
    elif cmove == "Paper" and p1move =="Rock":
        return cmove
    elif cmove == "Scissors" and p1move =="Paper":
        return cmove
    elif p1move == cmove:
        return ties
def get_full_move(shortmove):
    if p1move == "R" or "r" or "rock":
        return "Rock"
    if p1move == "P" or "p" or "paper":
        return "Paper"        
    if p1move == "S" or "s" or "scissors":
        return "Scissors"    
def print_score(pscore, cscore, ties):
    print("Scoreboard")
    print("----------")
    print("Player: {}".format(pscore))
    print("Computer: {}".format(cscore))
    print("Ties: {}".format(ties))
#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    print (get_rounds())
    print (get_p1_move())
    print (get_comp_move())
    print (print_score(p1move,cmove,ties))

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
def test():
    return 1
    #code here

rps()
