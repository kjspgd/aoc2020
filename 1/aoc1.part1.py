#!/usr/local/bin/python3


theNumbers = []

for line in open("input.txt"):
   theNumbers.append(int(line.rstrip()))


#print(theNumbers)

for number in theNumbers:
   #print(number)
   for sub_number in theNumbers:
      #print(sub_number)
      #print(str(number) + " + " + str(sub_number) + "=" + str(number + sub_number))
      if (number + sub_number == 2020):
         print(str(number) + " * " + str(sub_number) + " = " +  str(number * sub_number))
