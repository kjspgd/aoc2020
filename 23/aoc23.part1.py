



inputString = '219748365'
##sample inputString = '389125467'
theGame = []
for c in inputString: theGame.append(int(c))
#for i in range(10,1000001): theGame.append(int(i))


maxlen = len(theGame)
position = 0
activeCup = position

print(theGame)
for i in range(1,101):
    print("move " + str(i))
    print("The round Pre Move:" + str(theGame))
    #cupVal = int(theGame[position])
    cupVal = theGame[position]
    print("The current cupval is " + str(cupVal))
    #print(len(inputString))
    #input(cupVal)
    moveList = []
    movePos1 = int((position+1)%maxlen)
    moveList.append(theGame[movePos1])
    moveList.append(theGame[(movePos1+1)%maxlen])
    moveList.append(theGame[(movePos1+2)%maxlen])
    print("Pick up " + str(moveList))
    #input(moveList)
    theGame.pop(theGame.index(moveList[0]))
    theGame.pop(theGame.index(moveList[1]))
    theGame.pop(theGame.index(moveList[2]))
    destCupValue = 0
    #input(theGame)
    lcupVal = cupVal
    #print("---****____*****-----")
    #print("Starting with " + str (cupVal))
 ##Something here step 6
    while True:
        #print(((cupVal-1)%maxlen))
        candidate = int(((lcupVal-1)%maxlen))
        if candidate == 0: candidate =maxlen
        #print("Trying candidate " + str(candidate))
        if candidate in theGame:
            destCupValue = theGame[theGame.index(candidate)]
            break
        #print("Have to decrement")
        lcupVal -= 1
        #if lcupVal ==0 : lcupVal = maxlen
    print("Destination cup insert value " + str(destCupValue))
    #print("---****____*****-----")
    shortInsertPos = theGame.index(destCupValue)

    #input("Inserting here: " + str((shortInsertPos+1)%(len(theGame))))
    theGame.insert((shortInsertPos+1), moveList[0])
    theGame.insert((shortInsertPos+2), moveList[1])
    theGame.insert((shortInsertPos+3), moveList[2])
    print("The round Post Move:" + str(theGame))
    #position = (theGame.index(cupVal)+1)%maxlen
    #print("The dest cupval is " + str(destCupValue))
    #print("The current cupval is " + str(cupVal))
    #print("The current cup position is " + str(theGame.index(cupVal)))
    #print("the next posistion should be " + str(position))
    #
    #cupVal = destCupValue
    #print(theGame)
    #print(theGame.index(theGame[position]))
    position = (theGame.index(cupVal)+1)%maxlen
    print("---------------")


#print(theGame)
print("The End")
print(theGame)