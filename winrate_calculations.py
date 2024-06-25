import random

def bo1_premier_draft_wins(winrate):
    wins = 0
    loss = 0

    while True:
        num = random.random() * 100
        if num > (100 - winrate):
            wins += 1
        else:
            loss += 1
        
        if loss == 3 or wins == 7:
            break
        else: 
            pass
    
    return wins

