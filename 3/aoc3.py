#!/usr/local/bin/python3
count = 0
theLines = []

for line in open("input.txt"):
   theLines.append(line.rstrip())

theEntries=[[1,1],[3,1],[5,1],[7,1],[1,2]]
#theEntries = [[1,2]]

theResults = []
for entry in theEntries:
   xPos=1
   yPos=1
   xDelta = entry[0]
   yDelta = entry[1]

   for line in theLines:
      #print("\n")
      #print(str(xPos), str(yPos))
      #print ((yPos % yDelta) - (1 % yDelta))
      #print("YPosition:"+ str(yPos) + " " + str((yPos % yDelta) - (1 % yDelta)))   
      #print(str(len(line)))
      #print(str((line[(len(line) % xPos) - 1])) + " " + str(xPos % len(line))  + " " + str(xPos) + " " + str(count))
      #print(str(line[(xPos % len(line)) - 1]))
      if ((yPos % yDelta) - (1 % yDelta)) == 0:
         if "#" in line[(xPos % len(line)) - 1] and ((yPos % yDelta) - (1 % yDelta)) == 0 :
            count += 1
            #print("Hit")
         xPos += xDelta
      yPos += 1
   print(str(entry) + " " + str(count))
   theResults.append(count)
   count=0

finalResult = 1
for result in theResults: finalResult = finalResult * result

print("The resultant multiple is: " + str(finalResult))
