#!/usr/local/bin/python3


def wonkyEval(incomingString, parens=True):
   returnSum = 0
   if parens: incomingString = incomingString[1:-1]
#   input(incomingString)
   incomingString = reduceAddition(incomingString)
   returnSum = incomingString.split()[0]
   for i in range(1,len(incomingString.split())-1,2):
      returnSum = eval(str(returnSum) + incomingString.split()[i] + incomingString.split()[i+1])
   return returnSum


def reduceAddition(incomingString, parens=False):
   incomingList = incomingString.split()
#   if parens: incomingString = incomingString[1:-1]
#   input(incomingString)
   while True:
      if '+' not in incomingString:
         break
      incomingList = incomingString.split()
      for i in range(1, len(incomingList),2):
         if '+' in incomingList[i]:
            replaceString = str(incomingList[i-1]) + " " + str(incomingList[i]) + " " +str(incomingList[i+1])
            incomingString = incomingString.replace(replaceString,str(eval(replaceString)),1)
#            print(replaceString)
#            print("reduceAddition: " + incomingString)
            break
   return incomingString


def reduce(incomingString):
   while True:
      if '(' not in incomingString and ')' not in incomingString:
         break
#      print("reduce " + incomingString)
      gatherString = ''
      for char in incomingString:
#         print(len(gatherString))
         if len(gatherString) > 1 and ')' in str(char):
            gatherString += char
            break
         elif len(gatherString) == 0 and '(' in str(char):
            gatherString += char 
         elif len(gatherString) > 1 and '(' in str(char):
            gatherString = char
         elif len(gatherString) > 0 and '(' not in str(char):
            gatherString += char
      newVal = wonkyEval(gatherString, True)
      #print(str(newVal))
      #print(gatherString)
      incomingString = incomingString.replace(gatherString, str(newVal),1)
#      print(incomingString)
  # incomingString = reduceAddition(incomingString)
   #input(incomingString)
   #wonkyEval(incomingString,False)
   return wonkyEval(incomingString,False)



sum = 0
for line in open('input.txt','r'):
   tempSum = int(reduce(line))
   print(line + " " + str(tempSum))
   sum += tempSum

print("The sum is " + str(sum))
