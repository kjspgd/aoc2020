#!/usr/local/bin/python3


def wonkyEval(incomingString, parens=True):
   returnSum = 0
   if parens: incomingString = incomingString[1:-1]
   #input(incomingString)
   returnSum = incomingString.split()[0]
   for i in range(1,len(incomingString.split())-1,2):
      returnSum = eval(str(returnSum) + incomingString.split()[i] + incomingString.split()[i+1])
   return returnSum



def reduce(incomingString):
   while True:
      if '(' not in incomingString and ')' not in incomingString:
         break
      #print(incomingString)
      gatherString = ''
      for char in incomingString:
         #print(len(gatherString))
         if len(gatherString) > 1 and ')' in str(char):
            gatherString += char
            break
         elif len(gatherString) == 0 and '(' in str(char):
            gatherString += char 
         elif len(gatherString) > 1 and '(' in str(char):
            gatherString = char
         elif len(gatherString) > 0 and '(' not in str(char):
            gatherString += char
      newVal = wonkyEval(gatherString)
      #print(str(newVal))
      #print(gatherString)
      incomingString = incomingString.replace(gatherString, str(newVal))
   #input(incomingString)
   #wonkyEval(incomingString,False)
   return wonkyEval(incomingString,False)

  


#evalString = "(5 + 7 + 3 * (5 * 3 * 4 * 5) + 2 * 2) * 6 + (9 + 4 + (4 + 9 + 2 + 3) + 7 * 4 + (8 + 8)) + 6 + (7 + (5 + 2) + 2 * 8 + 9)"
#evalString  = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"

sum = 0
for line in open('input.txt','r'):
 sum += (reduce(line))

print("The sum is " + str(sum))
