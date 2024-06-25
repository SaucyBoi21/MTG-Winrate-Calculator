from draft_prizing import bo1_premier_draft_prizing
from winrate_calculations import bo1_premier_draft_wins

winrate = 68
gems = 0

count = 0
while (count < 100000):

    wins = bo1_premier_draft_wins(winrate)
    gems -= 1500
    gems += bo1_premier_draft_prizing(wins)
    print(f"Gems left: {gems}" )

    count += 1

