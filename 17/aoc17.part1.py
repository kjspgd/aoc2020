#!/usr/local/bin/python3
import time

def get_key(val, incDict):
    for key, value in incDict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def iterate():
   global xdgrid
   global gridDimension
   newgrid = []
   print("Starting iteration, length of grid " + str(len(xdgrid)))
   print("Starting iteration sum of " + str(getsum(xdgrid)))
   ##iter the global, process chars and repopulate the grid
   for z in range (0,gridDimension):
      for x in range (0, gridDimension):
         for y in range (0, gridDimension):
             newgrid.append([z,y,x,updatechar([z,y,x])])
   xdgrid = newgrid
   print("ending iteration, length of grid " + str(len(xdgrid)))
   print("ending iteration sum of " + str(getsum(xdgrid)))
   return 1

def getsum(incList):
   sum = 0
   for item in incList: sum+= item[3]
   return sum

def updatechar(incList):
   newState = 0
   global xdgrid
#   print(incList)
#   input()
   prevState = xdgrid[get_key(incList,lookupIndex)][3]
#   input(prevState)
   nbrcount = 0
   startz = incList[0]
   startx = incList[1]
   starty = incList[2]
   for varyz in range(startz-1,startz+2):
      for varyx in range(startx-1,startx+2):
         for varyy in range(starty-1,starty+2):
            try:
               #print("int the loop for " + str(varyz) + " " + str(varyx) + " " + str(varyy))
               nbrcount += xdgrid[get_key([varyz,varyx,varyy],lookupIndex)][3] 
            except: pass

   nbrcount -= prevState
   if prevState ==1:
      if nbrcount==2 or nbrcount==3:
         newState=1

   elif prevState == 0:
      if nbrcount == 3:
         newState=1
   return newState

debug = 1
theLines = []
xdgrid = []
iters = 6
lookupIndex = {}


for line in open("input.txt"):
   theLines.append(line.rstrip())

gridDimension = len(theLines) + (2 * iters) + 2 
if debug: print (gridDimension)

tempIndex = 0
for z in range (0,gridDimension):
   for x in range (0, gridDimension):
      for y in range (0, gridDimension):
          xdgrid.append([z,x,y,0])
          lookupIndex.update({tempIndex:[z,x,y]})
          tempIndex +=1
if debug:print(len(xdgrid))

midpoint = round(gridDimension/2)
linesmid = round(len(theLines)/2)

if debug:print(midpoint)
if debug:print(linesmid)

startInsertpoint = midpoint-linesmid

if debug:print(startInsertpoint)

startInsertx = startInsertpoint
startInserty = startInsertpoint
for line in theLines:
    startInserty = startInsertpoint
    for char in line:
       #remove the 0
       if '#' in char:
           xdgrid[get_key([midpoint,startInsertx,startInserty],lookupIndex)]=[midpoint, startInsertx, startInserty,1]
           #print("adding one at index " + str(get_key([midpoint,startInsertx,startInserty],lookupIndex)))
           #print(xdgrid[get_key([midpoint,startInsertx,startInserty],lookupIndex)])
       #append it
       startInserty +=1
    startInsertx +=1

##At this point we've initialized the grid and inserted the input roughly in the middle
startTime = time.time()
lastTime = time.time()
for i in range(1,7):
   print("--------------------------------")
   print("Starting iter " + str(i))
   print("Elapsed: " + str(time.time() - startTime))
   print("Iteration Delta: " + str(time.time() - lastTime))
   print("--------------------------------")
   lastTime = time.time()
   iterate()
