import random
def get_p1_move():
    p1move = input("Rock;Paper;Scissors: ")
    return p1move
def get_comp_move():
    cmove= random.choice( ['Rock', 'Paper', 'Scissors'] )
    return cmove
def get_rounds():
    user_rounds = int(input("Rounds: "))
    return user_rounds
def get_round_winner(p1move, cmove):
    if p1move == "Rock" and cmove == "Scissors":
        return "player"
    elif p1move == "Scissors" and cmove == "Paper":
        return "player"
    elif p1move == "Paper" and cmove == "Rock":
        return "player"
    elif cmove == "Rock" and p1move =="Scissors":
        return "comp"
    elif cmove == "Paper" and p1move =="Rock":
        return  "comp"
    elif cmove == "Scissors" and p1move =="Paper":
        return  "comp"
    elif cmove == p1move:
        return "tie"
def get_full_move(p1move):
    if p1move == "R" or p1move == "r" or  p1move == "rock":
        return "Rock"
    elif p1move == "P" or p1move == "p" or p1move == "paper":
        return "Paper"        
    elif p1move == "S" or p1move == "s" or p1move == "scissors":
        return "Scissors"    
    else:
        return "none"
def print_score(pscore, cscore, ties):
    print ("'''''''''")
    print("Scoreboard")
    print("----------")
    print("Player: {}".format(pscore))
    print("Computer: {}".format(cscore))
    print("Ties: {}".format(ties))
def rps():
    pscore = 0
    cscore = 0
    ties = 0
    for x  in range(get_rounds()):
        p1move = get_p1_move()
        cmove = get_comp_move()
        winner = get_round_winner(p1move,cmove)
        print ("Player chose {}".format(p1move))
        print ("Computer chose {}".format(cmove))
        if winner == "player":
            print ("Player win")
            pscore = pscore +1
            print_score(pscore,cscore,ties)
        elif winner == "comp":
            print("Computer win")
            cscore = cscore +1
            print_score(pscore,cscore,ties)
        elif winner == "tie":
            print("Its a tie")
            ties = ties + 1
            print_score(pscore,cscore,ties)
    if pscore > cscore:
        print ("Player won the game!")
    elif cscore > pscore:
        print ("Computer won the game!")
    else:
        print("Game is tied")
rps()
