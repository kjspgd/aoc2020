#!/usr/local/bin/python3
accumulator = 0

def parse(currindex,theLine):
   global accumulator
   #print(theLines.split()[int(currindex)])
   if 'nop' in str(theLine.split()[0]): 
      newIndex = currindex + 1
   if 'acc' in str(theLine.split()[0]):
      newIndex = currindex + 1
      accumulator += int(theLine.split()[1])
   if 'jmp' in str(theLine.split()[0]):
      newIndex = currindex + int(theLine.split()[1])
   #newIndex = currindex + 1
   print("new index is " + str(newIndex))
   return newIndex


theLines = []
theRunCommands = []
accumulator=0
index=0
previousIndex = 0
for readline in open("input.txt"):
   theLines.append(readline.rstrip())


     #index = parse(theLines[index]) 
#print(theLines)
for i in range(0,len(theLines)):
  previousIndex = index
  print("start for index is " + str(index))
  print(str(theLines[index]))
  print(str(theRunCommands.count(theLines[index])))
  if theRunCommands.count(index) != 0:
    break
  else:
    #print(theLines[i])
    index = parse(index,str(theLines[index]))
  print("Close for index is " + str(index) + " with a cum total of " + str(accumulator))
  theRunCommands.append(previousIndex)
print(str(accumulator))
