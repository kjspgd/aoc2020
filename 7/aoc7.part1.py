#!/usr/local/bin/python3
import sys

searchVal = 'shiny gold'
theAnswers = []


def iterator(topBag):
   returnVal = 0
   try:
      for item in theRules[topBag]:
         if returnVal == 0:
             if searchVal in item[0]:
                returnVal = 1
             else:
                returnVal = iterator(item[0])
   except:
      pass
   return returnVal;

theLines = []
count = 0
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
          subbags.append([contents.lstrip().rstrip().split()[0] + " " + contents.lstrip().rstrip().split()[1],110])
          print("exception no other " + str(contents.lstrip().rstrip().split()[0] + " " + contents.lstrip().rstrip().split()[1]))
       else:
          subbags.append([contents.lstrip().rstrip().split()[1] + " " + contents.lstrip().rstrip().split()[2],contents.lstrip().rstrip().split()[0]])
          print("exception single " + contents)
    else:
       for subbag in contents.split(","):
          subbags.append([subbag.lstrip().rstrip().split()[1] + " " + subbag.lstrip().rstrip().split()[2],subbag.lstrip().rstrip().split()[0]])
    theRules.update({topBag: subbags})
    #print(topBag + " --- ")
    #print(subbags)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

for topBag in theRules.keys():
   contains = 0
   contains = iterator(topBag)
   print("Contains! " + str(contains))
   if contains != 0:
       theAnswers.append(topBag)
       count += 1
       #print(topBag)
       #print(theRules[topBag])


print(theRules)
#print(theAnswers)
#print("Answer: " + str(count) + " or " + str(len(set(theAnswers))))
#print(theRules.keys())
