import random

def play():
    
    # Emojis
    emojis = ["", "✊", "🖐️", "✌️"]
     
    # User's choice
    print("1 is for “✊” (Rock). 2 is for “✋” (Paper).3 is for “✌” (Scissors).")
    user = int(input("What's your choice: "))
    
    # Computer's choice
    computer = random.randint(1, 3)
    
    print(f"You chose: {emojis[user]}")
    print(f"Computer chose: {emojis[computer]}")
    
    if user == computer:
        return "Draw"
    
    if win(user, computer):
        return "You win"
    
    return "You lost"
    
def win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if ( player == '1' and opponent == '3') or (player == '3' and opponent == '2') \
        or (player == '2' and opponent == '1'):
            return True

print(play())
