#!/usr/local/bin/python3


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
   theHist.update({item:[ii]}) 
#   lastNumber = item
   lastIndex = ii
   print("this round is " + str(ii))
lastNumber = 0
theHist.update({lastNumber:theHist[lastNumber] + [lastIndex+1]})
secondLast = 19999999
#input(theHist)
for index in range(len(theHist.keys())+2,30000001):
    newNumber = 0
  #  print("--------------")
#     print("Dealing with " + str(i))
    if lastNumber in theHist.keys(): 
       #print("this round is " + str(index) + " and We have a hit, last occurence of " + str(lastNumber) + " was at " + str(theHist[lastNumber]) + " so new number should be " + str(int(index) - int(lastIndex)))
       theLastIndexes = theHist[lastNumber]
#       print(theLastIndexes)
       if isinstance(theLastIndexes, int): 
          print("TheLastIndexes is a solo " + str(theLastIndexes))
       else:
          if(len(theLastIndexes)==1):
             #Last number was probably a recent add
             newNumber = 0
          else:
 #            print("Not a solo")
             myList = theHist[lastNumber]
             myList.sort(reverse=True)
             newNumber = myList[0] - myList[1]
  #           print("debug new number " + str(newNumber))
          if newNumber in theHist.keys():
             theHist.update({newNumber:theHist[newNumber] + [index]})
          else:
             theHist.update({newNumber:[index]})
          #print("is a list with max of " + str(myList[0]) + " and a second of " + str(myList[1]))
#       lastIndex = [theHist[lastNumber]].sort(reverse=True)[0]
#       input("Lastindex " + str(lastIndex) + " of " + str(lastNumber))
       #print(str(lastNumber) + " is in the table, now do something " + str(get_key(lastNumber, theHist)))
    else:
       newNumber = 0   
       theHist.update({newNumber:[index]})     
    lastNumber = newNumber
   # print(theHist)
    finalStr = ("Processed index " + str(index) + " this round value of " + str(newNumber))
    if index % 25000 == 0 : 
       print(finalStr)
  #  input("Close wait")
print(finalStr)
