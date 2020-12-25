#!/usr/local/bin/python3
import time
import collections


inputString = '219748365'
##sample inputString = '389125467'
theGame = []
for c in inputString: theGame.append(int(c))
#for i in range(10,1000001): theGame.append(int(i))
for i in range(10,1000001): theGame.append(int(i))

theGame = collections.deque(theGame)
maxlen = len(theGame)
position = 0
activeCup = position
startTime = time.time()
lastTime = time.time()
maxiter = 10000001
#maxiter = 100
modulo = 10000
debug = 0 
debugtime = 0 
dTime = time.time()

#print(theGame)
for i in range(1,maxiter):
    if i ==40000:
        debugtime = 2
        dTime = time.time()
    if i ==40002: debugtime = 0
    if debugtime: dTime = time.time()
    if i%modulo ==0:
        print("--------------------------------")
        print("Percent Complete: " + str((i/(maxiter-1))*100) + "%")
        print("Starting iter " + str(i))
        print("Elapsed: " + str(time.time() - startTime))
        print("Iteration Delta: " + str(time.time() - lastTime))
        deltaTime = time.time() - startTime
        predict = ((deltaTime*maxiter)/i) / 60 / 60
        print("Predicted overall completion Time: " + str(predict) + " hours")
        print("--------------------------------")
        lastTime = time.time()
    if debug: print("move " + str(i))
    if debug: print("The round Pre Move:" + str(theGame))
    #cupVal = int(theGame[position])
    cupVal = theGame[position]
    if debug: print("The current cupval is " + str(cupVal))
    #print(len(inputString))
    #input(cupVal)
    if debugtime == 2: print("Elapsed to point 1: " + str(time.time() - dTime))
    if debugtime ==2: dTime = time.time()
    moveList = []
    movePos1 = int((position+1)%maxlen)
    moveList.append(theGame[movePos1])
    moveList.append(theGame[(movePos1+1)%maxlen])
    moveList.append(theGame[(movePos1+2)%maxlen])

    if debugtime ==2: print("Elapsed to point 2: " + str(time.time() - dTime))
    if debugtime ==2: dTime = time.time()
    if debug: print("Pick up " + str(moveList))
    #input(moveList)
    #theGame.pop(theGame.index(moveList[0]))
    #theGame.pop(theGame.index(moveList[1]))
    #theGame.pop(theGame.index(moveList[2]))
    #theGame.remove(moveList[0])
    #theGame.remove(moveList[1])
    #theGame.remove(moveList[2])
    del theGame[movePos1]
    if movePos1==maxlen-1: movePos1 = 0
    del theGame[movePos1]
    if movePos1==maxlen-1: movePos1 = 0
    del theGame[movePos1]
    #del theGame[(movePos1+1)%maxlen]
    #del theGame[(movePos1+2)%maxlen]



    if debugtime ==2: print("Elapsed to point 3: " + str(time.time() - dTime))
    if debugtime ==2: dTime = time.time()
    destCupValue = 0
    #input(theGame)
    lcupVal = cupVal
    #print("---****____*****-----")
    #print("Starting with " + str (cupVal))
 ##Something here step 6
    shortInsertPos = 0
    while True:
        #print(((cupVal-1)%maxlen))
        candidate = int(((lcupVal-1)%maxlen))
        if candidate == 0: candidate =maxlen
        #print("Trying candidate " + str(candidate))
        if candidate not in moveList:
            shortInsertPos = theGame.index(candidate)
            destCupValue = theGame[shortInsertPos]
            break
        if debug: print("Have to decrement")
        lcupVal -= 1
        #if lcupVal ==0 : lcupVal = maxlen
    if debugtime ==2: print("Elapsed to point 4: " + str(time.time() - dTime))
    if debugtime ==2: dTime = time.time()
    if debug: print("Destination cup insert value " + str(destCupValue))
    #print("---****____*****-----")
    #shortInsertPos = theGame.index(destCupValue)

    #input("Inserting here: " + str((shortInsertPos+1)%(len(theGame))))
    theGame.insert((shortInsertPos+1), moveList[0])
    theGame.insert((shortInsertPos+2), moveList[1])
    theGame.insert((shortInsertPos+3), moveList[2])
    if debugtime ==2: print("Elapsed to point 5: " + str(time.time() - dTime))
    if debugtime ==2: dTime = time.time()
    if debug: print("The round Post Move:" + str(theGame))
    #position = (theGame.index(cupVal)+1)%maxlen
    #print("The dest cupval is " + str(destCupValue))
    #print("The current cupval is " + str(cupVal))
    #print("The current cup position is " + str(theGame.index(cupVal)))
    #print("the next posistion should be " + str(position))
    #
    #cupVal = destCupValue
    #print(theGame)
    #print(theGame.index(theGame[position]))
    if position < shortInsertPos and shortInsertPos < maxlen-3: 
       position = (position+1)%maxlen
    else:
       position = (theGame.index(cupVal)+1)%maxlen
    if debug: print("---------------")
    if debugtime ==2: print("Elapsed to point 6: " + str(time.time() - dTime))
    if debugtime ==2: dTime = time.time()

#print(theGame)
print("The End")
zeroIndex = theGame.index(1)
print("[1] index: " + str(theGame[(zeroIndex-0)%maxlen]))
print("[+1] index: " + str(theGame[(zeroIndex+1)%maxlen]))
print("[+2] index: " + str(theGame[(zeroIndex+2)%maxlen]))
