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

   return newIndex


theLines = []
theRunCommands = []
accumulator=0
index=0
for readline in open("input.txt"):
   theLines.append(readline.rstrip())


print(str(accumulator))
     #index = parse(theLines[index]) 
#print(theLines)
for i in range(0,len(theLines)):
  #print(theLines[i])
  index = parse(index,str(theLines[index]))
print(str(accumulator))
