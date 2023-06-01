import random

def play():
    print("Press R for ROCK")
    print("Press P for PAPER")
    print("Press S for Scissor")
    user = input()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's tie"
    
    if winner(user,computer):
        return "User wins"
    

    return 'User lost'
    

def winner(player,opponent):
    if(player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True
    


print(play())