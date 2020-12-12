#!/usr/local/bin/python3
import sys

searchVals = ['shiny gold']
theAnswers = []
count = 0


def iterator2(topBag):
    global count
    count +=1
    returnVal2 = 0
    for item in theRules[topBag]:
        if 'no other' in item[0]:
             print("Terminal: " + str(item))
             #count +=1
             returnVal2 = 1
        else:
             #print(str(item))
             #iterator2(item[0])
             #count += 1
             for i in range(0, int(item[1])-1):
                #count += int(iterator2(item[0])) * int(item[1])
                iterator2(item[0])
             returnVal2 += int(iterator2(item[0])) * int(item[1])
    print(str(returnVal2) + " is returnval for " + topBag + " for cumulative total of " + str(count))
    return returnVal2


theLines = []
for line in open("input.txt"):
   theLines.append(line.rstrip())

theRules = {} 
#print(theLines)

try:
  for line in theLines:
    topBag = (str(line.split()[0]) + " " + str(line.split()[1]))
    contents = str(line.split(" contain ")[1])
    subbags = [] 
    if "," not in contents:
       if "no other" in contents:
          subbags.append([contents.lstrip().rstrip().split()[0] + " " + contents.lstrip().rstrip().split()[1],0])
          #print(topBag)
          #print("exception no other " + str(contents.lstrip().rstrip().split()[0] + " " + contents.lstrip().rstrip().split()[1]))
       else:
          subbags.append([contents.lstrip().rstrip().split()[1] + " " + contents.lstrip().rstrip().split()[2],contents.lstrip().rstrip().split()[0]])
          #print("exception single " + contents)
    else:
       for subbag in contents.split(","):
          subbags.append([subbag.lstrip().rstrip().split()[1] + " " + subbag.lstrip().rstrip().split()[2],subbag.lstrip().rstrip().split()[0]])
    theRules.update({topBag: subbags})
    #print(topBag + " --- ")
    #print(subbags)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


for item in searchVals:
   iterator2(item)

#delete one because the top level shiny gold bag isn't included in the total
print(str(count-1))
