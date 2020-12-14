#!/usr/local/bin/python3

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

baseTest = 1
#y=5882352941176
#y=0
y=99999999999992
while True:
   #print(str(y))
   clearness = 0
   #print("Now I'll test for " + str(y))
   for z in range(1,len(myBuses)):
            if 'x' not in myBuses[z]:
                #print("Bus id " + str(myBuses[z]) + " will now test the first bus interval of " + str(y)  + " at offset " + str(z) + " which has an testing value of " + str(int(int(y)+int(z))))
                clearness += testTimestamp(int(y+z),myBuses[z])
                if clearness != 0: break
   if clearness ==0 : input("Hot dog we have a weiner at " + str(y))
   y += int(myBuses[0])
   #input("Move on to the next? " + str(clearness))
