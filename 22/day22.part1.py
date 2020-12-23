#!/usr/local/bin/python3

def fight(p1, p2):
    if debug: print(str(p1) + ' vs ' + str(p2))
    if p1 > p2: return 1
    if p2 > p1: return 2

def calcScore(incList):
    score = 0
    incList = sorted(set(incList), key=lambda i: incList[::-1].index(i), reverse=True)
    x = len(incList)
    for item in incList:
        if debug: print(str(x) + '\t' + str(item))
        score += x * int(item)
        x -= 1
    return score

debug = 0
player1 = 0
player2 = 0
player1hand = []
player2hand = []
for line in open('input.txt'):
    if('Player 1:') in line.rstrip(): player1 = 1; player2 = 0
    elif('Player 2:') in line.rstrip(): player1 = 0; player2 = 1
    elif player1 and len(line.rstrip()) != 0: player1hand.append( line.rstrip())
    elif player2 and len(line.rstrip()) != 0: player2hand.append(line.rstrip())
if debug: print(len(player1hand))
if debug: print(len(player2hand))


score = 0
p1index = 0
p2index = 0
winner = 0
round = 0
while True:
    round += 1
    if len(player1hand) == p1index :
        print("Player 2 Winner")
        print('Score ' + str(calcScore(player2hand)))
        break
    if len(player2hand) == p2index:
        print("Player 1 Winner")
        print('Score ' + str(calcScore(player1hand)))
        break
    roundResult = fight(int(player1hand[p1index]), int(player2hand[p2index]))
    if debug: print(str(round) + ' winner is ' + str(roundResult))
    if roundResult == 1:
        player1hand.append(player1hand[p1index])
        player1hand.append(player2hand[p2index])
        #player2hand.remove(player2hand[p2index])
        #p1index += 1
    elif roundResult == 2:
        player2hand.append(player2hand[p2index])
        player2hand.append(player1hand[p1index])
        #player1hand.remove(player1hand[p1index])
        #p2index += 1
    p1index += 1
    p2index += 1
    if debug: print("ending " + str(len(player1hand)) + " " + str(len(player2hand)))
    #input('anotha round')


