#!/usr/local/bin/python3

with open("input.txt", "a") as file:
  file.write("\n")

file.close()

sum=0
cumulline=''
for line in open("input.txt"):
   #print(str(len(line)))
   if len(line) != 1:
      #print("not yet")
      cumulline += line.rstrip()
   else:
      print(str(len(set(cumulline))) + " " + cumulline)
      #print(cumulline)
      sum += len(set(cumulline))
      cumulline=''


print(str(sum))
