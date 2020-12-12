#!/usr/local/bin/python3
accumulator = 0

def parse(currindex,theLine):
   global accumulator
   global theLines
   if 'nop' in str(theLine.split()[0]):
      #if currindex + int(theLine.split()[1]) <= (len(theLines)) and currindex + int(theLine.split()[1]) >= (len(theLines)-6): print("Change this line: " + theLine) 
      newIndex = currindex + 1
   if 'acc' in str(theLine.split()[0]):
      newIndex = currindex + 1
      accumulator += int(theLine.split()[1])
   if 'jmp' in str(theLine.split()[0]):
      #if currindex + 1 <= (len(theLines)-1) and currindex + 1 >= (len(theLines)-6): print("Change this line: " + theLine)
      newIndex = currindex + int(theLine.split()[1])
   #print("new index is " + str(newIndex))
   return newIndex


def test(testIndex):
  global accumulator
  accumulator = 0
  index = 0
  newPassable = []
  #if 'acc in str(theLines[testIndex][0]):
  #   break
  #else:
  iteratedlines = 0
  for i in range(0,1000):
        iteratedlines = i
        #print(str(theLines[index]))
        if index == testIndex:
            if 'nop' in str(theLines[index]):
                #print('nop match')
                newPassable = 'jmp ' + str(theLines[index]).split()[1]
                index = parse(index,newPassable)
            if 'jmp' in str(theLines[index]):
                newPassable = 'nop' + str(theLines[index]).split()[1]
                index = parse(index,newPassable)
        else:
           index = parse(index,str(theLines[index]))
        if index == len(theLines)-1 : print("Hot Dog at index " + str(index) + " of line " + theLines[testIndex] + " with an accumulation of " + str(accumulator))
  return iteratedlines

theLines = []
theRunCommands = []
accumulator=0
index=0
previousIndex = 0
for readline in open("input.txt"):
   theLines.append(readline.rstrip())

#print("The len of theLines is " + str(len(theLines)))
     #index = parse(theLines[index]) 
#
#while True:
#  previousIndex = index
#  index = parse(index,str(theLines[index]))
#  theRunCommands.append(previousIndex)
#print(str(accumulator))

resultcount = 0
for i in range(0,len(theLines)-1):
   resultcount = test(i)
#   print("Testing " + str(i) + " results in " + str(resultcount))
   if resultcount < 999: print("Hey we got a match at line " + str(i))
