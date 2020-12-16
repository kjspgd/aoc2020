#!/usr/local/bin/python3
import time

startTime = time.time()
theHist = {}

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"


for line in open("input.txt"):
  for number in line.rstrip().split(","):
    theHist.update({int(number):0})

#preinit the file
ii=0
lastNumber = 0
for item in theHist:
   ii+=1
   theHist.update({item:ii}) 
#   lastNumber = item
   lastIndex = ii
   print("this round is " + str(ii))
lastNumber = 0
#theHist.update({lastNumber:lastIndex+1})
#print(theHist)
lastTime = time.time()
for index in range(len(theHist.keys())+2,30000001):
    newNumber = 0
    if lastNumber not in theHist.keys():
       #print("Not in list") 
       theHist.update({lastNumber:index-1})
       newNumber = 0
    else:
       #print("In list")
       newNumber = (index-1) - theHist[lastNumber]
       theHist.update({lastNumber:index-1})
       #print(newNumber)
    lastNumber = newNumber
 
    #print(theHist)
    finalStr = ("Processed index " + str(index) + " this round value of " + str(newNumber))
    if index % 250000 == 0:
       print(finalStr)
       print("Elapsed: " + str(time.time() - startTime))
       print("Delta: " + str(time.time() - lastTime))
       print("--------------------------------")
       lastTime = time.time()

  #  input("Close wait")
print(finalStr)
