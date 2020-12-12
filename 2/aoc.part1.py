#!/usr/local/bin/python3


theLines = []

for line in open("input.txt"):
   theLines.append(line.rstrip())
count = 0
for line in theLines:
   min = line.split()[0].split("-")[0]
   max = line.split()[0].split("-")[1]
   char = line.split()[1].split(":")[0]
   pwd = line.split()[2]
   occurences = pwd.count(char)
   if((pwd.count(char) >= int(line.split()[0].split("-")[0])) and (pwd.count(char) <= int(line.split()[0].split("-")[1]))):
      print(str(occurences) + " " + min + " " + max + " " + char + " " + pwd)
      count += 1

print(str(count))
