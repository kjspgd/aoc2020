#!/usr/local/bin/python3

validRanges ={} 
myTicket = []
neighborTickets = []

myTicketState = 0
nearbyTicketState = 0
for line in open("input.txt"):
   if len(line) == 1:
      myTicketState = 0
      nearbyTicketState = 0
   if ' or ' in line: 
      tempList = []
      tempList.clear()
      name = line.lstrip().rstrip().split(':')[0]
      range1 = line.lstrip().rstrip().split(':')[1].split(' or ')[0]
      range2 = line.lstrip().rstrip().split(':')[1].split(' or ')[1]
      for i in range(int(range1.split('-')[0]), int(range1.split('-')[1])+1):
          tempList.append(i)    
      for i in range(int(range2.split('-')[0]), int(range2.split('-')[1])+1):
         #print(item)
          tempList.append(i)
      validRanges.update({name:tempList})
      #print(line)
      #input(str(validRanges[name]))
      #validRanges.append(line.lstrip().rstrip().split(':')[1].split(' or ')[0])
      #validRanges.append(line.lstrip().rstrip().split(':')[1].split(' or ')[1])
   if 'your ticket' in line:
      myTicketState = 1
   if 'nearby tickets' in line:
      nearbyTicketState = 1
   if myTicketState and ':' not in line:
      for item in line.rstrip().split(','): myTicket.append(item)
   if nearbyTicketState and ':' not in line:
      tempList = []
      for item in line.rstrip().split(','): 
          tempList.append(item)
      neighborTickets.append(tempList)

validNumbers = []
for item in validRanges.values():
   for subitem in item: validNumbers.append(subitem)

legitTickets = []
for item in neighborTickets:
   legitness = 1
   #print(item)
   for number in item:
     if int(number) not in validNumbers: legitness = 0

   if legitness == 1: 
      print("Legit")
      legitTickets.append(item)
   else:
      print("Not legit")

   #print(validNumbers) 

#print(legitTickets)
#
print(validRanges.keys())
print(len(legitTickets))
#input("wait")

validIndexes = {} 
for fieldtype in validRanges.keys():
   tempList = []
   for column in range(0,len(legitTickets[0])):
      tempList.append(column)
   validIndexes.update({fieldtype:tempList})

#input(str(validIndexes))

for column in range(0,len(legitTickets[0])):
  #print("processing column " + str(column))  
  for fieldtype in validRanges.keys():
     workingValidIndexes = validIndexes[fieldtype]
     #print("Now processing " + str(fieldtype))
     #print(validRanges[fieldtype])
     possibilities = 0
     for ticket in legitTickets:
        #print("processing column " + str(column) +  " fieldtype of " + fieldtype + " for number " + str(ticket[column]))
        if int(ticket[column]) in validRanges[fieldtype]: 
           possibilities +=1
        else:
           print("Column " + str(column) + " can't be " + str(fieldtype))
           workingValidIndexes.remove(column)
     validIndexes.update({fieldtype:workingValidIndexes})

iterCount = len(validIndexes.keys()) -1
singleCount = 0

multiplyList = []
while singleCount < len(validIndexes.keys())-1:
 singleCount = 0
 for item in validIndexes.keys():
   if len(validIndexes[item]) == 1:
      singleCount += 1
      if 'departure' in str(item): multiplyList.append(validIndexes[item][0])
      print("It is proven valid index for " + str(item) + " is " + str(validIndexes[item][0]))
      for iter in validIndexes.copy().keys():
         if iter not in item:
            tempList = validIndexes[iter]
            try:
              tempList.remove(validIndexes[item][0])
            except: pass
            validIndexes.update({iter:tempList})
#  input(str(iterCount))


for item in validIndexes.keys():
   print(str(item) + " " + str(validIndexes[item]))

multiplyList = set(multiplyList)
print(multiplyList)

result = 1
for item in multiplyList:
   result = result * int(myTicket[item])

print("The final answer is " + str(result))
