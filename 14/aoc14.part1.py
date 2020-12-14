#!/usr/local/bin/python3


theLines = []
debug = 0

def eval(maskin, intin):
   calcedInt = 0
   global debug
   binIn = bin(intin)[2:].zfill(36)
   if debug: print(str(binIn) + " << Original" )
   if debug: print(str(maskin) + " << Mask")
   outbin = '' 
   for i in range(0,len(maskin)):
      if maskin[i] != 'X':
          outbin += maskin[i]
      else:
          outbin += binIn[i]
   if debug: print(str(outbin) + " << calced")
   calcedInt=int(outbin, 2)
   if debug: print(str(int(outbin, 2)))
   return calcedInt

for line in open("input.txt"):
   theLines.append((line.rstrip()))


#print(theLines)
lastMask = ''
registers = {}
for line in theLines:
   if 'mask =' in line:
      if debug: print("Here's a mask: " + line.split()[2])
      lastMask = line.split()[2]
   else:
      returnVal = 0
      register = line.split()[0][4:len(line.split()[0])-1]
      evalNo = int(line.split()[2])
      if debug: print("A register at " + register + " for " + line.split()[0] + " with an eval of " + str(evalNo))
      returnVal = eval(lastMask, evalNo)
      if debug: print("Write " + str(returnVal) + " at register " + str(register))
      registers.update({register:returnVal})

if debug: print(registers)
if debug: print(len(registers))
if debug: print(len(theLines))
total = 0
for item in registers.values():
   total += item

print("The total is " + str(total))
