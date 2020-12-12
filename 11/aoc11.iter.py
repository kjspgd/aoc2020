#!/usr/local/bin/python3


theGrid = []
bufferedGrid = []
theLines = []
filler = '#'
buffer = 4 
for line in open("input_sample.txt"):
   theGrid.append(list(line.rstrip()))
   #mapArray.insert(list(line.rstrip()))
   #print((list(line.rstrip())))

for i in range(0,(len(theGrid)+int(2*buffer)-1)):
#   print(i)
   line = ''
   if i < buffer: line = filler * (len(theGrid[0])+int(2*buffer)) 
   elif i >= (len(theGrid)+int(buffer)): line = filler * (len(theGrid[0])+int(2*buffer))
   else:
      for z in range(0,(len(theGrid[0])+int(2*buffer))):
         #print("Entering " + str(i) + " " + str(z))
         #print(theGrid[i][z-int(buffer/2)])
         if z < buffer: line = line + filler
         elif z >= len(theGrid[0])+int(buffer): line = line + filler
         else: line = line + (theGrid[i-buffer][z-buffer])
         #else: print(str(i) + " " + str(z))
   bufferedGrid.append(list(line))
print(bufferedGrid[10][6])

