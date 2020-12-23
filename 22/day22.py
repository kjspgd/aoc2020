#!/usr/local/bin/python3

def fight(fp1hand, fp1index, fp2hand, fp2index):
    winner = 0
    fp1 = int(fp1hand[fp1index])
    fp2 = int(fp2hand[fp2index])
    if debug: print(str(fp1) + ' vs ' + str(fp2))
    if fp1 < len(fp1hand)-int(fp1index) and fp2 < len(fp2hand)-int(fp2index):
    #    print("Creating subgame")
    #    print(fp1hand.copy()[fp1index+1:fp1index+1+fp1])
    #    print(fp2hand.copy()[fp2index+1:fp2index+1+fp2])
        #p1hand = sorted(set(p1hand), key=lambda i: p1hand[::-1].index(i), reverse=True)
        #p2hand = sorted(set(p2hand), key=lambda i: p2hand[::-1].index(i), reverse=True)
        winner = playGame(fp1hand.copy()[fp1index + 1:fp1index+1+fp1], fp2hand.copy()[fp2index+1:fp2index+1+fp2])[0]
        #print("winner is " + str(winner))
    else:
        if fp1 > fp2: winner = 1
        if fp2 > fp1: winner = 2
    #print("fightwinner " + str(winner))
    return winner


def calcScore(incList):
    score = 0
    #print(len(incList))
    incList = sorted(set(incList), key=lambda i: incList[::-1].index(i), reverse=True)
    x = len(incList)
    #print(x)
    for item in incList:
        if debug: print(str(x) + '\t' + str(item))
        score += x * int(item)
        x -= 1
    return score

def playGame(p1hand=[], p2hand=[]):
    global gamecount
    gamecount  += 1
    gameid = gamecount
    #print(p1list)
    #print(p2list)
    #print("Game starting number " + str(gamecount))
    playedHands = []
    score = 0
    p1index = 0
    p2index = 0
    winner = 0
    round = 0
    eject = 0
    while True:
        round += 1
        roundText = ''
        p1cardcount = len(p1hand)-p1index
        p2cardcount = len(p2hand)-p2index

     #   print(roundText)
        try:
            roundText = str(p1hand[p1index]) + "v" + str(p2hand[p2index])
            if p1cardcount: roundText = str(p1hand[-p1cardcount:])
            roundText += 'v'
            if p2cardcount: roundText += str(p2hand[-p2cardcount:])
            #input(roundText)
        except:
            if debug: print("Uh oh " + str(p1index) + ' of ' + str(p1hand) + " ---- " + str(p2index) + ' of ' + str(p2hand))
            if len(p1hand) == p1index :
                if debug:print("uh oh Player 2 Winner")
                #print('Score ' + str(calcScore(player2hand)))
                score = calcScore(p2hand)
                winner=2
                break
            if len(p2hand) == p2index:
                if debug: print("uh oh Player 1 Winner")
                #print('Score ' + str(calcScore(player1hand)))
                score = calcScore(p1hand)
                winner=1
                break
            pass

        if roundText in playedHands:
 #           print(roundText)
#            print(playedHands)
#            print("eject!")
            eject = 1
            score = calcScore(p1hand)
            winner = 1
            break
        if len(p1hand) == p1index :
            #print("Player 2 Winner")
            #print('Score ' + str(calcScore(player2hand)))
            score = calcScore(p2hand)
            winner=2
            break
        if len(p2hand) == p2index:
            #print("Player 1 Winner")
            #print('Score ' + str(calcScore(player1hand)))
            score = calcScore(p1hand)
            winner=1
            break

        if roundText not in '': playedHands.append(roundText)
        #roundResult = fight(int(player1hand[p1index]), int(player2hand[p2index]))
        roundResult = fight(p1hand, p1index, p2hand, p2index)
    #    print("Round result = " + str(roundResult))
        #print(str(round) + ' winner is ' + str(roundResult))
        if roundResult == 1:
            #print("Here")
            p1hand.append(p1hand[p1index])
            p1hand.append(p2hand[p2index])
            #player2hand.remove(player2hand[p2index])
            #p1index += 1
        elif roundResult == 2:
            #print("here 2")
            p2hand.append(p2hand[p2index])
            p2hand.append(p1hand[p1index])
            #player1hand.remove(player1hand[p1index])
            #p2index += 1
        else:
            print("Something wonky occured")
            print(p1hand)
            print(p2hand)
            input("enter to continue")

        p1index += 1
        p2index += 1
        if gameid == 1: print("ending round of game " + str(gameid) + ' roundwinner ' + str(roundResult) + ' ' + str(len(p1hand) - p1index) + ' ' + str(len(p2hand)-p2index))
        #input('anotha round')
#    print("ending game " + str(gameid) + ' winner ' + str(winner))
    #print("exiting game" + str(gameid))
    if debug:print((len(p1hand)))
    if debug:print(p1index)
    if debug:print(len(p1hand) - p1index)
    if len(p1hand) - p1index and debug: print(p1hand[(len(p1hand)-p1index):])
    if debug:print(p1hand)
    if len(p2hand) - p2index and debug: print(p2hand[-(len(p2hand)-p2index):])
    if debug:print('---')
    if debug:
        for item in sorted(set(p1hand), key=lambda i: p1hand[::-1].index(i), reverse=True)[-50:]:
           print(item)
    if debug:print('---')
    return [winner,score]

debug = 0
player1 = 0
player2 = 0
player1hand = []
player2hand = []
gamecount = 0
for line in open('input.txt'):
    if('Player 1:') in line.rstrip(): player1 = 1; player2 = 0
    elif('Player 2:') in line.rstrip(): player1 = 0; player2 = 1
    elif player1 and len(line.rstrip()) != 0: player1hand.append( line.rstrip())
    elif player2 and len(line.rstrip()) != 0: player2hand.append(line.rstrip())

answer = playGame(player1hand, player2hand)
print("Winner is " + str(answer[0]) + " with a score of " + str(answer[1]))
