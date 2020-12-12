#!/usr/local/bin/python3


theLines = []

for line in open("input.txt"):
   theLines.append(line.rstrip())
count = 0
for line in theLines:
   pos1 = int(line.split()[0].split("-")[0]) - 1
   pos2 = int(line.split()[0].split("-")[1]) - 1
   char = line.split()[1].split(":")[0]
   pwd = line.split()[2]
#   print(str(pos1))
#   print(str(pwd.index(pos1)))
#   print(str(pwd))
#   print("\n")
   occurences = 0
   runcount = 0
   try:
      if char in pwd[pos1]:
           occurences += 1
      else:
           runcount +=1
   except:
      print(char + " caused exception at " + line.split()[0].split("-")[0] + " in " + pwd)
      #print(str(len(pwd)) + " " + str(pos1))
      pass

   try:
      if char in pwd[pos2]:
           occurences += 1
      else:
           runcount += 1

   except:
      print(char + " caused exception at " + line.split()[0].split("-")[1] + " in " + pwd)
      #print(str(len(pwd)) + " " + str(pos1))
      pass

   if occurences==1:
      count += 1

#         print("Hey, first position match " + char + " at " + str(int(line.split()[0].split("-")[0])) + " " + str(pwd[pos1-1]) + str(pwd[pos1]) + str(pwd[pos1+1]) + " " + pwd[int(pos1)] + " " + pwd)
         #print("Matchy")
         #print(char + " matchy at " + str(int(line.split()[0].split("-")[0])) + " in " + pwd)
         #count +=1 
   #if((pwd.count(char) >= int(line.split()[0].split("-")[0])) and (pwd.count(char) <= int(line.split()[0].split("-")[1]))):
   #   print(str(occurences) + " " + min + " " + max + " " + char + " " + pwd)
   #   count += 1
print(str(count))
