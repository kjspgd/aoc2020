#!/usr/local/bin/python3
import re
with open("input.txt", "a") as file:
  file.write("\n")

file.close()
part1sum=0
sum=0
cumulline=''
reqItems = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
validEcl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
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
         tempDict.update({item.split(":")[0]: item.split(":")[1]})
      print(str(len(list(set(tempItems) & set(reqItems)))))
      if len(list(set(tempItems) & set(reqItems))) == 7:
         invalid = 0
         #It's part 1 valid.
         part1sum +=1
         if not (re.search(r"^[1][9][2-9][0-9]$|[2][0][0][1-2]$",tempDict["byr"])): invalid += 1
         if not (re.search(r"^[2][0][1][0-9]$|[2][0][2][0]$",tempDict["iyr"])): invalid += 1
         if not (re.search(r"^[2][0][2][0-9]$|[2][0][3][0]$",tempDict["eyr"])): invalid += 1

         if not (re.search(r"^[#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$",tempDict["hcl"])): invalid += 1
        
         if not (re.search(r"^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$",tempDict["pid"])): invalid += 1
#         heightVal = tempDict["hgt"][:len(tempDict["hgt"]) -2]
#         print(str(heightVal))
         if ("cm" in tempDict["hgt"]):
             if not (re.search(r"^[1][5-8][0-9]$|^[1][9][0-3]$",tempDict["hgt"][:len(tempDict["hgt"]) -2])): print("cm err"); invalid += 1
#            print(tempDict["hgt"][:len(tempDict["hgt"]) -2])
         elif ("in" in tempDict["hgt"]):
             if not (re.search(r"^[5][9]$|^[6][0-9]$|^[7][0-6]$",tempDict["hgt"][:len(tempDict["hgt"]) -2])): print("in err"); invalid += 1
#            print(tempDict["hgt"][:len(tempDict["hgt"]) -2]

         if tempDict["ecl"] not in validEcl: invalid += 1

         if invalid==0:
            sum += 1
#            print(str(tempDict["hgt"]))
      cumulline=''
      
print("part 1 " + str(part1sum))
print(sum)
