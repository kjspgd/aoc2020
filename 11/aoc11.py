#!/usr/local/bin/python3


bareGrid = []
bufferedGrid = []
theLines = []
filler = '.'
buffer = 1 

def pad(incomingGrid):
   tempGrid = []
   global buffer
   global filler
   for i in range(0,(len(incomingGrid)+int(2*buffer))):
   #   print(i)
      line = ''
      if i < buffer: line = filler * (len(bareGrid[0])+int(2*buffer)) 
      elif i >= (len(incomingGrid)+int(buffer)): line = filler * (len(incomingGrid[0])+int(2*buffer))
      else:
         for z in range(0,(len(incomingGrid[0])+int(2*buffer))):
#            print("Entering " + str(i) + " " + str(z))
            #print(incomingGrid[i][z-int(buffer/2)])
            if z < buffer: line = line + filler
            elif z >= len(incomingGrid[0])+int(buffer): line = line + filler
            else: 
               if 'L' in incomingGrid[i-buffer][z-buffer]: line = line + '#'
               else: line = line + (incomingGrid[i-buffer][z-buffer])
      #print(line)
      tempGrid.append(list(line))
   debugPrintGrid(tempGrid, 'Before returning pad')
   return tempGrid

def update(updateincomingGrid):
   debugPrintGrid(updateincomingGrid, 'Update incoming')
   newGrid = []
#   newGrid.clear()
#   newGrid = updateincomingGrid.copy()
   for x in range (0,len(updateincomingGrid)):
      lineAppender=[]
      for y in range (0, len(updateincomingGrid[x])):
#         newGrid[x][y] = checkSeat([x,y],updateincomingGrid.copy())
         lineAppender.append(checkSeat([x,y],updateincomingGrid.copy()))
      newGrid.append(lineAppender)
   debugPrintGrid(newGrid, 'Update Outgoing')
   return newGrid

def checkSeat(coord,checkSeatincomingGrid):
#   print(coord)
#   print(checkSeatincomingGrid)
   newSeatType =  checkSeatincomingGrid[coord[0]][coord[1]] 
#   print(checkSeatincomingGrid[coord[0]][coord[1]])     
   adjacentList = []
   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]-i
         newy = coord[1]-i  
#         print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy]) 
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)

   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]-i
         newy = coord[1]
#         print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)

   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]-i
         newy = coord[1]+i
#         print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)



   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]
         newy = coord[1]-i
#         print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)


   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]
         newy = coord[1]+i
#         print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)



   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]+i
         newy = coord[1]-i
#         print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)



   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]+i
         newy = coord[1]
 #        print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)


   try:
      appender = '.'
      for i in range(1,125):
         newx = coord[0]+i
         newy = coord[1]+i
  #       print(str(newx) + " " + str(newy) + " " + checkSeatincomingGrid[newx][newy])
         if(('#' in checkSeatincomingGrid[newx][newy]) or ('L' in checkSeatincomingGrid[newx][newy])):
            if(newx>0 and newy>0):
               appender = (checkSeatincomingGrid[newx][newy])
               break
   except:
      pass
   adjacentList.append(appender)


   if len(adjacentList) != 8: input("whoopsy " + ' '.join(map(str,adjacentList)))
#   print(str(coord[0]) + " " + str(coord[1]) + " " + str(adjacentList))
#   print(' '.join(map(str,adjacentList)))
#   #input("shitshow")

   if('.' in checkSeatincomingGrid[coord[0]][coord[1]]):
      newSeatType = checkSeatincomingGrid[coord[0]][coord[1]]
 #     print(checkSeatincomingGrid[coord[0]][coord[1]] + " is floor, do nothing")
   elif ('#' in checkSeatincomingGrid[coord[0]][coord[1]]):
 #     print( " " + checkSeatincomingGrid[coord[0]][coord[1]] + " is occupied. It has " + str(adjacentList.count("#")) + " occupied neighbors")
      if(adjacentList.count("#") >= 5): 
 #        print("Too crowded, Change seat to empty!")
         newSeatType = 'L'
   elif ('L' in checkSeatincomingGrid[coord[0]][coord[1]]):
 #     print( " " + checkSeatincomingGrid[coord[0]][coord[1]] + " is open. It has " + str(adjacentList.count("#")) + " occupied neighbors")
      if(adjacentList.count("#") == 0): 
 #         print("Change seat to occupied!")
          newSeatType = "#"
   else:
      input("Exception!")
   checkSeatincomingGrid.clear()
   return newSeatType   

def countOccupied(countoccupiedincomingGrid):
   occupied =0
   for x in range (0,len(countoccupiedincomingGrid)):
      for y in range (0, len(countoccupiedincomingGrid[x])):
         if '#' in countoccupiedincomingGrid[x][y]: occupied += 1
   return occupied

def debugPrintGrid(kjsGrid, tempText=''):
 #   print("-----------start debug " + tempText + "---------------")
 #   for x in range (0,len(kjsGrid)):
 #      line = ''
 #      for y in range (0, len(kjsGrid[x])):
 #         line = line + str(kjsGrid[x][y])
 #      print(line)
 #   print("-----------end debug " + tempText + "-----------------")
    return 1


for line in open("input.txt"):
   bareGrid.append(list(line.rstrip()))
   #mapArray.insert(list(line.rstrip()))
   #print((list(line.rstrip())))


bufferedGrid = pad(bareGrid)
debugPrintGrid(bufferedGrid, 'ONSTART')
#print("Old grid")
#print(bufferedGrid)
#print("\n\n\n")
#newGrid = update(bufferedGrid)
#print("New Grid")
#print(newGrid)
runcount = 0

onceMore=0
while True:
   if (runcount==0): previousGrid = bufferedGrid.copy()
   else: previousGrid = currentGrid.copy()
   previousCount = countOccupied(previousGrid)
   runcount +=1 
   print("Runcount: " + str(runcount))
   currentGrid = update(previousGrid).copy()
   #print(previousGrid)
   #print(currentGrid)
   #input("wait")
   currentCount = countOccupied(currentGrid)
   #print("Old occupied " + str(previousCount))
   #print("New occupied " + str(currentCount))
   #print("\t" + str(previousCount - currentCount))
   #debugPrintGrid(previousGrid, 'WHILELOOP-PREVIOUS')
   #debugPrintGrid(currentGrid, 'WHILELOOP-CURRENT')   
   #input("Cycle through shitshow")
   if (previousCount - currentCount) == 0: input("Hot Dog" + str(currentCount)) 
   

   '''
   newGrid = update(oldGrid).copy()
   newCount = countOccupied(newGrid)
   print("Old occupied " + str(oldCount))
   print(oldGrid)
   #newGrid = update(oldGrid)
   print(newGrid)
   print("New occupied " + str(newCount))
   if(oldCount == newCount):
   #if(countOccupied(newGrid)==countOccupied(oldGrid)):
      print(newGrid)
      input("Wait! Hot dog!")
   '''
