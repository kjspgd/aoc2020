#!/usr/local/bin/python3


theLines = []
xpos=0
ypos=0
wayxpos = 10
wayypos = 1

currDirection = int(0)
theDirections = ['N','E','S','W']
for line in open("input.txt"):
   theLines.append(line.rstrip())


#print(theLines)
for line in theLines:
   currDirection = int(0)
   part1 = line[0]
   part2 = int(line[1:])
   print(line[1:])
   if part1 in 'F': 
      #part1 = theDirections[int(currDirection)]
      xpos = xpos + (wayxpos * int(part2))
      ypos = ypos + (wayypos * int(part2))
   if part1 in 'N': wayypos += part2
   if part1 in 'S': wayypos -= part2
   if part1 in 'E': wayxpos += part2
   if part1 in 'W': wayxpos -= part2
   if part1 in 'R': 
      currDirection += abs((int(part2) / 90))
      currDirection = currDirection % 4
   if part1 in 'L': 
      currDirection -= abs((int(part2) / 90))
      currDirection = currDirection % 4
   if currDirection != 0:
      oldwayxpos = wayxpos
      oldwayypos = wayypos
      if currDirection == 1:
         wayxpos = oldwayypos
         wayypos = (-1) * oldwayxpos
      if currDirection == 2:
         wayxpos = (-1) * oldwayxpos
         wayypos = (-1) * oldwayypos
      if currDirection == 3:
         wayxpos = (-1) * oldwayypos
         wayypos = oldwayxpos
   
   print("Directions are " + line[0] + "," + str(line[1]) + " which results in a postion of " + str(xpos) + "," + str(ypos) + " with a waypoin position of " + str(wayxpos) + " " + str(wayypos))
   #input("anotha one")
print("Manhattan coordinates = " + str(abs(xpos) + abs(ypos)))
