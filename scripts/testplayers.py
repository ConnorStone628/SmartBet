
from random import randint
import scoring
import lineup


players = []
positions = ['C', 'F1', 'F2', 'D1', 'D2', 'D3', 'G', 'R1', 'R2', 'R3', 'R4', 'T', 'S']

# for i in range(200):
#     x = {'Id':i}
#     x['Score'] = randint(4,9)
#     x['Salary'] = randint(3000, 7000)
#     x['Position'] = positions[randint(0,len(positions)-1)].strip('0123456789')
#     players.append(x)

# with open('players.txt','w') as f:
#     for p in players:
#         f.write(str(p) + '\n')

players = {}
with open('players.txt', 'r') as f:
    for p in f.readlines():
        player = eval(p)
        players[player['Id']] = player

bscore = scoring.BasicScoring(players, [])

blineup = lineup.BasicLineup(bscore.GenerateRoster(), positions, {'Budget':30000})

newlineup =  blineup.GenerateLineup()

newteam = newlineup.GetPlayers()

total = 0
for p in newteam:
    total += newteam[p]['RosterScore']
    print newteam[p]

print total
    
    
