#!/usr/local/bin/python3

validRanges = []
myTicket = []
neighborTickets = []

myTicketState = 0
nearbyTicketState = 0
for line in open("input.txt"):
   if len(line) == 1:
      myTicketState = 0
      nearbyTicketState = 0
   if ' or ' in line: 
      validRanges.append(line.lstrip().rstrip().split(':')[1].split(' or ')[0])
      validRanges.append(line.lstrip().rstrip().split(':')[1].split(' or ')[1])
   if 'your ticket' in line:
      myTicketState = 1
   if 'nearby tickets' in line:
      nearbyTicketState = 1
   if myTicketState and ':' not in line:
      for item in line.rstrip().split(','): myTicket.append(item)
   if nearbyTicketState and ':' not in line:
      for item in line.rstrip().split(','): neighborTickets.append(item)

validNumbers = []

for item in validRanges:
    for i in range(int(item.split('-')[0]),int(item.split('-')[1])+1): validNumbers.append(int(i))

#print(validNumbers)

sum =0
for item in neighborTickets:
   if int(item) not in validNumbers:
      print("Not valid number: " + str(item))
      sum += int(item)

print("The ticket scanning error rate is " + str(sum))
'''
print("Ranges")
print(validRanges)
print("--------")
print("My")
print(myTicket)
print("--------")
print("Ranges")
print(neighborTickets)
print("--------")
'''
