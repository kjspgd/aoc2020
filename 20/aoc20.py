#!/usr/local/bin/python3

def getEdges(incList):
   newList = []
   #first line and reverse
   newList.append(incList[:1][0])
   newList.append(incList[:1][0][::-1])
   #last line and reverse
   newList.append(incList[-1:][0])
   newList.append(incList[-1:][0][::-1])

   # Get the edges
   sfirstCol = ''
   slastCol = ''
  #for col in range(0,len(incList)+1):
   for item in incList:
      sfirstCol += item[0]
      slastCol += item[len(item)-1]
   newList.append(sfirstCol)
   newList.append(sfirstCol[::-1])
   newList.append(slastCol)
   newList.append(slastCol[::-1])  
   
   return newList





theTiles={}
tileField = 0
tileTitle = 1
for line in open("input.txt"):
   if 'Tile' in line:
      tileNo = line.rstrip().split()[1][:-1]
      tileTitle == 0
      tileField = 1
      tempField = []
   elif len(line.rstrip()) == 0:
      theTiles.update({tileNo:tempField})
      tileTitle = 1
      tileField = 0
   elif tileField:
      tempField.append(line.rstrip())
   else:
      input("Something weird happened")

validEdges = []
for item in theTiles.keys():
   print("Tile number " + str(item))
   #for line in theTiles[item]:
   #   print(line)
   for edge in getEdges(theTiles[item]): validEdges.append(edge)


#print(validEdges)
result = 1
for item in theTiles.keys():
   count = 0
   for edge in getEdges(theTiles[item]): 
      count += validEdges.count(edge)
   if count == 12:  
      result *= int(item)
      print("Corner Tile number " + item + " matches: " + str(count))

print("/nFinal answer: " + str(result))
