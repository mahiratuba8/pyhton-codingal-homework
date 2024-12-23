import random

def player():
    user= input("whats your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    user= user.lower()

    computer= random.choice(['r','p','s'])
    
    if user==computer:
        return "You and the computer have both chosen {}. Its a tie.".format(computer)
    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen{}. You have won".format(user, computer)
    return "You have chosen {} and computer has chosen {}. You lost:(".format(user,computer)

def is_win(player, opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p')or (player=='p' and opponent=='r'):
        return True
    return False

if __name__== '__main__':
    print(player())