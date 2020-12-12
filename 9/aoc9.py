#!/usr/local/bin/python3


theLines = []
buffer=25
goldenValue=29221323

def getSums(inboundList):
   returnList=[]
   midsum = 0
   theAyes = []
   for i in inboundList:
       midsum += int(i)
       theAyes.append(int(i))
       if midsum == goldenValue: 
          print("dingding " + str(theAyes))
          print(str(min(theAyes)) + " + " + str(max(theAyes)) + " = " + str(min(theAyes)+max(theAyes)))
          input("Hot dog")

   return returnList

for line in open("input.txt"):
   theLines.append(line.rstrip())




for testLine in range(0,len(theLines)):
   tested = []
   tested = getSums(theLines[int(testLine):int(len(theLines))])

