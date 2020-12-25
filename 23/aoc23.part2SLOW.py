
import time

def getIndexes(incList):
    if debug: print("The length of incoming list " + str(len(incList)))
    if debug: print("The length of unique  in incoming list " + str(len(set(incList))))
    theDict = {}
    for i in range(0,len(incList)):
        theDict.update({incList[i]:int(i)})
    if debug: print("The length of outgoing dict " + str(len(theDict)))
    return theDict

inputString = '219748365'
##sample inputString = '389125467'
theGame = []
for c in inputString: theGame.append(int(c))
for i in range(10,1000001): theGame.append(int(i))


maxlen = len(theGame)
print("Maxlen = " + str(maxlen))
position = 0
activeCup = position
debug = 1
#if debug: print(theGame)
startTime = time.time()
lastTime = time.time()
maxiter = 10000001
modulo = 1000
for i in range(1,maxiter):
    if i%modulo ==0:
        print("--------------------------------")
        print("Percent Complete: " + str((maxiter/modulo)*100) + "%")
        print("Starting iter " + str(i))
        print("Elapsed: " + str(time.time() - startTime))
        print("Iteration Delta: " + str(time.time() - lastTime))
        deltaTime = time.time() - lastTime
        predict = deltaTime * (maxiter/modulo)
        print("Predicted overall completion Time: " + str(predict))
        print("--------------------------------")
        lastTime = time.time()

    indexDict = getIndexes(theGame)
    if i != 1: position = (indexDict[cupVal]+1)%maxlen
    if debug: print("move " + str(i))
    #if debug: print("The round Pre Move:" + str(theGame))
    #cupVal = int(theGame[position])
    cupVal = theGame[position]
    if debug: print("The current cupval is " + str(cupVal))
    #print(len(inputString))
    #input(cupVal)
    moveList = []
    movePos1 = int((position+1)%maxlen)
    moveList.append(theGame[movePos1])
    moveList.append(theGame[(movePos1+1)%maxlen])
    moveList.append(theGame[(movePos1+2)%maxlen])
    if debug: print("Pick up " + str(moveList))
    if debug: print("Len of DictIndex " + str(len(indexDict)))
    #input(moveList)
    ##theGame.pop(theGame.index(moveList[0]))
    ##theGame.pop(theGame.index(moveList[1]))
    ##theGame.pop(theGame.index(moveList[2]))
    print(indexDict[moveList[0]])
    theGame.pop(indexDict[moveList[0]])
    theGame.pop(indexDict[moveList[1]])
    theGame.pop(indexDict[moveList[2]])
    destCupValue = 0
    #input(theGame)
    lcupVal = cupVal
    #print("---****____*****-----")
    #print("Starting with " + str (cupVal))
 ##Something here step 6
    indexDict = getIndexes(theGame)
    while True:
        #print(((cupVal-1)%maxlen))
        candidate = int(((lcupVal-1)%maxlen))
        if candidate == 0: candidate =maxlen
        #print("Trying candidate " + str(candidate))
        if candidate in theGame:
            destCupValue = theGame[indexDict[candidate]]
            break
        #print("Have to decrement")
        lcupVal -= 1
        #if lcupVal ==0 : lcupVal = maxlen
    if debug: print("Destination cup insert value " + str(destCupValue))
    #print("---****____*****-----")
    shortInsertPos = indexDict[destCupValue]

    #input("Inserting here: " + str((shortInsertPos+1)%(len(theGame))))
    theGame.insert((shortInsertPos+1), moveList[0])
    theGame.insert((shortInsertPos+2), moveList[1])
    theGame.insert((shortInsertPos+3), moveList[2])
    #if debug: print("The round Post Move:" + str(theGame))
    #position = (theGame.index(cupVal)+1)%maxlen
    #print("The dest cupval is " + str(destCupValue))
    #print("The current cupval is " + str(cupVal))
    #print("The current cup position is " + str(theGame.index(cupVal)))
    #print("the next posistion should be " + str(position))
    #
    #cupVal = destCupValue
    #print(theGame)
    #print(theGame.index(theGame[position]))
    #position = (theGame.index(cupVal)+1)%maxlen
    if debug: print("---------------")


#print(theGame)
print("The End")
print(theGame)