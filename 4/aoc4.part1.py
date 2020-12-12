#!/usr/local/bin/python3

with open("input.txt", "a") as file:
  file.write("\n")

file.close()

sum=0
cumulline=''
reqItems = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
for line in open("input.txt"):
   #print(str(len(line)))
   if len(line) != 1:
      cumulline += line.rstrip() + " "
   else:
      print(cumulline)
      lineList = []
      lineList = cumulline.split()
      tempItems = []
      tempDict = {}
      for item in lineList:
         tempItems.append(item.split(":")[0])
         tempDict.update({item})
      print(str(len(list(set(tempItems) & set(reqItems)))))
      if len(list(set(tempItems) & set(reqItems))) == 7:
         #It's part 1 valid.
         print(tempDict)
         sum += 1
      cumulline=''
      

print(sum)
