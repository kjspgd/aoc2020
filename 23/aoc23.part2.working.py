#!/usr/local/bin/python3

import time
import collections

def nicePrint(incDict):
   val = 1
   prstr = ''
   for i in range(0,len(incDict)):
       prstr += str(incDict[val]) + ", "
       val = incDict[val]
       i += 1
   print(prstr)

##real
inputString = '219748365'
##sample
#inputString = '389125467'
theGame = []
gameDict = {}
gameList = []
for c in inputString: theGame.append(int(c))

for i in range(10,1000001): theGame.append(int(i))
#for i in range(10,21): theGame.append(int(i))

for i in range(0,len(theGame)-1):
    gameDict.update({int(theGame[i]):int(theGame[i+1])})
gameDict.update({theGame[len(theGame)-1]:int(inputString[0])})
#input(gameDict)

maxlen = len(theGame)
#cupVal = gameDict[0]
cupVal = int(inputString[0])
print(cupVal)
position = int(0)

startTime = time.time()
lastTime = time.time()
maxiter = 10000001
#maxiter = 10
modulo = 2500000
debug = 0
debugtime = 0
dTime = time.time()
for i in range(0,maxiter):
   if i%modulo ==0:
      print("--------------------------------")
      print("Percent Complete: " + str((i/(maxiter-1))*100) + "%")
      print("Starting iter " + str(i))
      print("Elapsed: " + str(time.time() - startTime))
      print("Iteration Delta: " + str(time.time() - lastTime))
      #deltaTime = time.time() - startTime
      #predict = ((deltaTime*maxiter)/i) / 60 / 60
      #print("Predicted overall completion Time: " + str(predict) + " hours")
      #print("--------------------------------")
      lastTime = time.time()
   #print("--------------------------------------")
   #nicePrint(gameDict)
   #print("Active cup value is " + str(cupVal))
   remove1 = gameDict[cupVal]
   remove2 = gameDict[remove1]
   remove3 = gameDict[remove2]
   #print("Remove is " + str(remove1))
   #print("Remove is " + str(remove2))
   #print("Remove is " + str(remove3))
   lcupVal = cupVal
   while True:
      #print(((cupVal-1)%maxlen))
      candidate = int(((lcupVal-1)%maxlen))
      #print("Trying candidate " + str(candidate))
      if candidate == 0: candidate = maxlen
      if candidate==remove1 or candidate==remove2 or candidate==remove3:
          #print("Have to decrement")
          lcupVal -= 1
      else:
          destCupValue = candidate
          break



   #print("Destination is " + str(destCupValue))
   ##ONLY NOW DO UPDATES HERE
   activeCup = cupVal
   newCupVal = gameDict[remove3]
   #activecup
   gameDict.update({activeCup:gameDict[remove3]})
   cupVal = gameDict[remove3]
   #move3
   gameDict.update({remove3:gameDict[destCupValue]})
   #destination cup
   gameDict.update({destCupValue:remove1})
   cupVal = newCupVal

   #input("test")

   #position = gameList[position][1]
print("The end")
#nicePrint(gameDict)
#print(gameDict)
one=gameDict[1]
two=gameDict[one]

print("Just after one: " + str(one))
print("Two after one: " + str(two))
print("Result is: " + str(one*two))

'''
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
        #debugtime = 1
        #dTime = time.time()
        lastTime = time.time()
    if debug: print("move " + str(i))
    if debug: print("The round Pre Move:" + str(theGame))
    #cupVal = int(theGame[position])
    cupVal = theGame[position]
    if debug: print("The current cupval is " + str(cupVal))
    #print(len(inputString))
    #input(cupVal)
    if debugtime: input("Elapsed to point 1: " + str(time.time() - dTime))
    if debugtime: dTime = time.time()
    moveList = []
    movePos1 = int((position+1)%maxlen)
    moveList.append(theGame[movePos1])
    moveList.append(theGame[(movePos1+1)%maxlen])
    moveList.append(theGame[(movePos1+2)%maxlen])

    if debugtime: input("Elapsed to point 2: " + str(time.time() - dTime))
    if debugtime: dTime = time.time()
    if debug: print("Pick up " + str(moveList))
    #input(moveList)
    #theGame.pop(theGame.index(moveList[0]))
    #theGame.pop(theGame.index(moveList[1]))
    #theGame.pop(theGame.index(moveList[2]))
    theGame.remove(moveList[0])
    theGame.remove(moveList[1])
    theGame.remove(moveList[2])

    if debugtime: input("Elapsed to point 3: " + str(time.time() - dTime))
    if debugtime: dTime = time.time()
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
    if debugtime: input("Elapsed to point 4: " + str(time.time() - dTime))
    if debugtime: dTime = time.time()
    if debug: print("Destination cup insert value " + str(destCupValue))
    #print("---****____*****-----")
    shortInsertPos = theGame.index(destCupValue)

    #input("Inserting here: " + str((shortInsertPos+1)%(len(theGame))))
    theGame.insert((shortInsertPos+1), moveList[0])
    theGame.insert((shortInsertPos+2), moveList[1])
    theGame.insert((shortInsertPos+3), moveList[2])
    if debugtime: input("Elapsed to point 5: " + str(time.time() - dTime))
    if debugtime: dTime = time.time()
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
    position = (theGame.index(cupVal)+1)%maxlen
    if debug: print("---------------")
    if debugtime: input("Elapsed to point 6: " + str(time.time() - dTime))
    if debugtime: dTime = time.time()

#print(theGame)
print("The End")
zeroIndex = theGame.index(1)
print("[1] index: " + str(theGame[(zeroIndex-0)%maxlen]))
print("[+1] index: " + str(theGame[(zeroIndex+1)%maxlen]))
print("[+2] index: " + str(theGame[(zeroIndex+2)%maxlen]))
'''
