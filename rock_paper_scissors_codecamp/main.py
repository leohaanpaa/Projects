import random

def play():
    
    # User's choice
    user = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors: ")
    
    # Computer's choice
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "Draw"
    
    if win(user, computer):
        return "You win"
    
    return "You lost"
    
def win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if ( player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True

print(play())
