#!/usr/local/bin/python3

def beforeAfter(incomingList):
   delta = 0
   lastitem = 0
   icount = 0
   bcount = 0
   for item in incomingList:
      delta = item - lastitem
#      if lastitem != 0:
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
theLines = []
with open("input.txt") as theFile:
  for line in theFile:
     theLines.append(int(line.rstrip()))
theLines.sort()
beforeAfter(theLines)
#print(theLines)
