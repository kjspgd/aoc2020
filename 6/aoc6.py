#!/usr/local/bin/python3

with open("input.txt", "a") as file:
  file.write("\n")

file.close()

sum=0
cumulline=''
commonanswers=[]
newsetindicator = True
for line in open("input.txt"):
   #print(str(len(line)))
   if len(line) != 1:
      #print("not yet")
      cumulline += line.rstrip()
      currentline = []
      currentline = list(line.rstrip())
      if newsetindicator:
         commonanswers = currentline
      else:
         commonanswers = set(currentline) & set(commonanswers)
      print(commonanswers)
      newsetindicator = False
   else:
      #print(str(len(set(cumulline))) + " " + cumulline)
      #print(cumulline)
      sum += len(commonanswers)
      print(str(len(commonanswers)) + " " + cumulline)
      commonanswers = []
      cumulline=''
      newsetindicator = True

print(sum)
