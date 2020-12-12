#!/usr/local/bin/python3
count = 0
theLines = []
xPos=1
for line in open("input.txt"):
   theLines.append(line.rstrip())

for line in theLines:
   #print(str(len(line)))
   print(str((line[(len(line) % xPos) - 1])) + " " + str(xPos % len(line))  + " " + str(xPos) + " " + str(count))
   if "#" in line[(xPos % len(line)) - 1]:
      count += 1
   xPos +=1
print(count)
