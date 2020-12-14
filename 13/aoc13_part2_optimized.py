#!/usr/local/bin/python3
import math
import time
import sys

def findNext(interval):
   if 'x' not in interval:
      testingInterval = 0
      global myTimestamp
      while testingInterval < myTimestamp:
         testingInterval += int(interval)
      #input("The last interval we tested is " + str(testingInterval)) 
      myWait = int(testingInterval) - int(myTimestamp)
      myProduct = int(interval) * myWait
      print("Bus ID " + str(interval) + " wait is " + str(myWait) + " with a product of " + str(myProduct)) 


def testTimestamp(timeStamp,busid):
      modulus = 0
      modulus = int(timeStamp) % int(busid)
      return modulus


myTimestamp = 0
myBuses = []
i = 0
for line in open("input.txt"):
   if i==0: myTimestamp = int((line.rstrip()))
   else: myBuses = line.rstrip().split(",")
   i+=1
#print("My timestamp is " + str(myTimestamp))
#print("My buses are " + str(myBuses))
mymax = 0
mymaxIndex = 0
secondmax = 0
secondmaxIndex = 0
thirdmax = 0
thirdmaxIndex = 0
sortableListtocheck = []
sortableListtocheck = myBuses.copy()
sortableListtocheck[:] = [x for x in sortableListtocheck if x != 'x']
sortableListtocheck.sort(reverse=True)
mymax = int(sortableListtocheck[0])
secondmax = int(sortableListtocheck[1])
thirdmax = int(sortableListtocheck[2])
for index in range(0,len(myBuses)):
   if 'x' not in (myBuses[index]):
      if int(myBuses[index]) == mymax: mymaxIndex=index
      if int(myBuses[index]) == secondmax: secondmaxIndex=index
      if int(myBuses[index]) == thirdmax: thirdmaxIndex=index

baseTest = 1
print("My max " + str(mymax) + " is at index " + str(mymaxIndex) + " and second max " + str(secondmax) +  " at index " + str(secondmaxIndex))

startInt = 0
floor = 100000000000000

startInt = (math.floor(floor/mymax) * mymax) + mymax
#print("Start at " + str(startInt))
y=startInt
counter = 1 
startTime = time.time()
clearness = 0  
debug = 0 
theWiener = 0
lasttwopair = 0
lasttwopairdelta = 0
yy=0
#while True:
finderrc =0
startPos = 0
while True:
   if testTimestamp(int(yy)-int(mymaxIndex)+int(secondmaxIndex), myBuses[secondmaxIndex])==0:
      if testTimestamp(int(yy)-int(mymaxIndex)+int(thirdmaxIndex), myBuses[thirdmaxIndex])==0:
         if finderrc == 0 : startPos = int(yy)
         lasttwopairdelta = int(yy)-int(mymaxIndex)-lasttwopair
         finderrc += 1
         if finderrc > 9: break
         lasttwopair = int(yy)-int(mymaxIndex)
         #break
   yy += int(myBuses[mymaxIndex])
print("last - to be used - twopairdelta " + str(lasttwopairdelta))
#print("left the break")
#y=math.floor(lasttwopair / startInt) * lasttwopair
y=startPos
print("twopair offset - first instance at timestamp " + str(y))
#y = startInt = (math.floor(floor/lasttwopairdelta) * lasttwopairdelta) + lasttwopairdelta
#input("twopair floored Start at " + str(y))
print("Commencing much math")
while True:
   if y == 842186186521918 : 
      print("At least we're trying")
      debug = 1
   if y > 842186186521935: 
      print("good god too far")
      print(str(y))
      input("ahh")
   if counter % 10000000 == 0 : 
      print("Tests Performed:  " + str(counter))
      print(str(y))
      executionTime = (time.time() - startTime)
      print('Execution time in seconds: ' + str(executionTime))
      startTime = time.time()
   if True:
         clearness = 0 
         theWiener = 0
         for z in range(0,len(myBuses)):
            if debug: print("all the thirds")
            timestamptotest = int(y)-int(mymaxIndex)+int(z)
            #print(str(y) + " zval " + str(z) + " timestamp " + str(timestamptotest))
            if z == 0: theWiener = timestamptotest
            if 'x' not in myBuses[z]:
               if debug: print(str(myBuses[z]) + " at z of " + str(z))
               clearness += testTimestamp(timestamptotest,myBuses[z])
               if debug: print("all the thirds and clearness " + str(clearness) + " for " +str(z))
            if clearness != 0: break
         if clearness ==0 : 
            print("Hot dog we have a weiner at timestamp " + str(theWiener))
            sys.exit()
         y += int(lasttwopairdelta)
   counter +=1
   debug = 0
#   input("Move on to the next at " + str(y) + " clearness of " + str(clearness))
