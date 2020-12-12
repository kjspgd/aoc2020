#!/usr/local/bin/python3

def howManyOptions(testingNumber):
  global theLines
  #print(testingNumber)
  #subList = [i for i in theLines if ((i >= (testingNumber-3)) and (i <= (testingNumber+3))) and (i!=testingNumber)]
  subList=[]
  for subitem in theLines:
     if (subitem >= (testingNumber-3)) and (subitem <= (testingNumber+3)) and (subitem!=testingNumber):
        subList.append(subitem)
        print("Testing " + str(testingNumber) + " and there are " + str(len(set(subList))) + " options now in the set: " + str(subList))
  print("so now I'm returning " + str(len(set(subList))))
  #input("Wait.")

  return len(set(subList))

def beforeAfter(incomingList):
   delta = 0
   lastitem = 0
   icount = 0
   bcount = 0
   for item in incomingList:
      delta = item - lastitem
      if lastitem != 0:
        if delta == 1: 
            icount +=1
        if delta == 3: 
            bcount +=1
      else: print("do you want to play repeat")
      lastitem = item
      print(str(lastitem) + "\t" + str(item) + "\t" + str(delta) + "\t" + str(icount) + "\t" + str(bcount))
   print("The 1 count: ", str(icount))
   print("The 3 count: ", str(bcount))
   print("The product is: ", str(icount * (bcount+1)))
   return delta


def findChunks(incomingList):
   foo = 0
   totalOptions = 1
   lastitem = 0
   chunkList = [] 
   calcedOptions = 1
   for item in incomingList:
     #print(" item is " + str(item) + " and last item is " + str(lastitem))
     if item - lastitem >= 3:
        #print("A chunk occureth!")
        if len(chunkList) == 3: calcedOptions = 2
        if len(chunkList) == 4: calcedOptions = 4
        if len(chunkList) == 5: calcedOptions = 7
        if len(chunkList) > 5: input("Oh crap")
        print(str(chunkList) + " which has these many options: " + str(calcedOptions))
        totalOptions = totalOptions * calcedOptions
        chunkList.clear()
        chunkList.append(item)
        calcedOptions = 1
     else:
        chunkList.append(item)
     lastitem = item
   #Deal with the last one now
   if len(chunkList) == 3: calcedOptions = 2
   if len(chunkList) == 4: calcedOptions = 4
   if len(chunkList) == 5: calcedOptions = 7
   print(str(chunkList) + " which has these many options: " + str(calcedOptions))
   totalOptions = totalOptions * calcedOptions
   print("The total number of options is " + str(totalOptions))
   return foo



theLines = []
theLines.append(0)
with open("input.txt") as theFile:
  for line in theFile:
     theLines.append(int(line.rstrip()))
theLines.sort()
theLines.append(max(theLines)+3)
#beforeAfter(theLines)
#options = 1 
#for item in theLines:
#   options = options * howManyOptions(item)

#print(options)

findChunks(theLines)
