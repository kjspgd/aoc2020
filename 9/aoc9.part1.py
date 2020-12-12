#!/usr/local/bin/python3


theLines = []
buffer=25


def getSums(inboundList):
   returnList=[]
   for i in inboundList:
       print("iterating " + str(i))
       for z in inboundList:
           if i != z:
               returnList.append(int(i)+int(z))

   returnList.sort()
   return returnList

for line in open("input.txt"):
   theLines.append(line.rstrip())

for testLine in range(0+buffer, len(theLines)):
   print("Testing line " + str(testLine) + " range starting " + theLines[int(testLine-buffer)] + " ending " + theLines[int(testLine-1)])
   resultantList = getSums(theLines[int(testLine-buffer):int(testLine)])
   print(resultantList)
   if int(theLines[testLine]) in resultantList: 
      print("Matchy on " + theLines[testLine] + " index at " + str(testLine))
   else: 
      print("Dingdingdingdingding" + theLines[testLine] + " index at " + str(testLine))
     # print(resultantList)
      input("Enter to return")

#      print(testLine) 
#   print(getSums(theLines[int(testLine-buffer):int(testLine-1)]))
#   print(len(getSums(theLines[int((testLine-buffer)):int((testLine-1))])))

#print(getSums(theLines))
#print(theLines)


